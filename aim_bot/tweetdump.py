#!/usr/bin/env python

import tweepy
import configparser
import pprint
import argparse
import requests
import traceback
import elasticsearch
import json
from datetime import timezone, datetime


class StreamTweets(tweepy.StreamListener):
    def __init__(self, webhook, debug, elastic_index, es_host_list):
        super().__init__()
        self.webhook = webhook
        self.debug = debug
        self.elastic_index = elastic_index

        if len(es_host_list) > 0:
            self.es = elasticsearch.Elasticsearch(es_host_list)
        else:
            self.es = elasticsearch.Elasticsearch()

    def on_status(self, status):
        if self.debug:
            pprint.pprint(repr(status))

        # TODO: can be replaced with chatbot alert library later when it is complete
        if self.webhook is not None:
            try:
                embed_blob = {}
                fields = []
                embed_blob['title'] = "@{}".format(status.user.screen_name)
                embed_blob['thumbnail'] = {"url": status.user.profile_image_url_https}
                tweet_time = status.created_at.replace(tzinfo=timezone.utc).astimezone(tz=None)
                fields.append({"name": "Timestamp", "value": str(tweet_time)})
                fields.append({"name": "Status", "value": status.text})

                if 'media' in status.entities:
                    embed_blob['image'] = {"url": status.entities['media'][0]["media_url_https"]}

                if 'urls' in status.entities and len(status.entities['urls']):
                    urls = []
                    for u in status.entities['urls']:
                        urls.append(u['expanded_url'])
                    fields.append({"name": "Expanded URLs", "value": str(urls)})

                embed_blob["fields"] = fields

                result = requests.post(self.webhook, json={"username": "Twitter Monitor", "embeds": [embed_blob]})

                if result.status_code != 204:
                    print("[{}] - {}".format(result.status_code, result.text))

            except:
                print(traceback.format_exc())

        if self.elastic_index is not None:
            try:
                status_obj = status._json
                status_obj['timestamp'] = datetime.utcnow()
                self.es.index(index="tweets", doc_type="tweet", body=status_obj)
            except:
                print(traceback.format_exc())

        else:
            pprint.pprint(repr(status))


def dump_twitter(screen_name, count=100, include_rts=0):
    # TODO: Re-implement with Tweepy and validate dump limit
    # tweets = t_client.statuses.user_timeline(include_rts=include_rts, screen_name=screen_name, count=count)
    # for tweet in tweets:
    #     print(json.dumps(tweet))
    pass


def setup_elastic_index(es_host_list):
    if len(es_host_list) > 0:
        elastic = elasticsearch.Elasticsearch(es_host_list)
    else:
        elastic = elasticsearch.Elasticsearch()

    try:
        mapping = {
            "tweet": {
                "properties": {
                    "timestamp": {"type": "date"},
                }
            }
        }

        elastic.indices.create("tweets")
        elastic.indices.put_mapping(index="tweets", doc_type="tweet", body=mapping)

    except:
        print(traceback.format_exc())


def stream_twitter(username_list, webhook, debug, elastic, elastic_hosts):
    userid_list = []

    for username in username_list:
        userid_list.append(str(api.get_user(username).id))

    tweet_listener = StreamTweets(webhook, debug, elastic, elastic_hosts)
    tweet_stream = tweepy.Stream(auth=api.auth, listener=tweet_listener, es_host_list=elastic_hosts)
    tweet_stream.filter(userid_list)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="tcpdump style tool for twitter. can stream tweets or dump profiles")
    parser.add_argument('config', help='Config file name')
    parser.add_argument('--userlist', help="List of target user names", nargs='+', required=True)
    parser.add_argument('--dump', help='Dump a full twitter profile.', action='store_true')
    parser.add_argument('--stream', help='Stream tweets as they come in to stdout or other destinations', action='store_true')
    parser.add_argument('--retweets', help='Include retweets in a dump', action='store_true')
    parser.add_argument('--count', help='Number of tweets to pull down when dumping')
    parser.add_argument('--webhook', help='Webhook to dump messages to')
    parser.add_argument('--elastic', help='Save tweets to ElasticSearch index', action="store_true")
    parser.add_argument('--debug', help="Print lots of extra stuff for debugging", action='store_true')
    parser.add_argument('--buildindex', help="Build the ElasticSearch index and mapping", action='store_true')
    opts = parser.parse_args()

    config = configparser.RawConfigParser()
    config.read(opts.config)
    consumer_key = config.get("Twitter", "consumer_key")
    consumer_secret = config.get("Twitter", "consumer_secret")
    access_token = config.get("Twitter", "access_token")
    access_secret = config.get("Twitter", "access_secret")
    es_host_list = json.loads(config.get("Elastic", "host_list"))

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)

    if opts.buildindex:
        setup_elastic_index(es_host_list)

    if opts.stream:
        stream_twitter(opts.userlist, webhook=opts.webhook, debug=opts.debug, elastic=opts.elastic,
                       elastic_hosts=es_host_list)

    # TODO: Re-implement with Tweepy and validate dump limit
    # if opts.dump:
    #     if opts.retweets:
    #         include_retweets = 1
    #     else:
    #         include_retweets = 0
    #
    #     if opts.count is not None:
    #         dump_twitter(opts.user, count=opts.count, include_rts=include_retweets)
    #     else:
    #         dump_twitter(opts.user, include_rts=include_retweets)
