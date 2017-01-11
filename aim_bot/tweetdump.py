#!/usr/bin/env python

import tweepy
import configparser
import pprint
import argparse
import requests
import traceback
from datetime import timezone


class StreamTweets(tweepy.StreamListener):
    def __init__(self, webhook, debug):
        super().__init__()
        self.webhook = webhook
        self.debug = debug

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
        else:
            pprint.pprint(repr(status))


def stream_twitter(username_list, webhook, debug):
    userid_list = []

    for username in username_list:
        userid_list.append(str(api.get_user(username).id))

    tweet_listener = StreamTweets(webhook, debug)
    tweet_stream = tweepy.Stream(auth=api.auth, listener=tweet_listener)
    tweet_stream.filter(userid_list)


def dump_twitter(screen_name, count=100, include_rts=0):
    # TODO: Re-implement with Tweepy and validate dump limit
    # tweets = t_client.statuses.user_timeline(include_rts=include_rts, screen_name=screen_name, count=count)
    # for tweet in tweets:
    #     print(json.dumps(tweet))
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="tcpdump style tool for twitter. can stream tweets or dump profiles")
    parser.add_argument('config', help='Config file name')
    parser.add_argument('--userlist', help="List of target user names", nargs='+', required=True)
    parser.add_argument('--dump', help='Dump a full twitter profile.', action='store_true')
    parser.add_argument('--stream', help='Dump a full twitter profile.', action='store_true')
    parser.add_argument('--retweets', help='Include retweets in a dump', action='store_true')
    parser.add_argument('--count', help='Number of tweets to pull down when dumping')
    parser.add_argument('--webhook', help='Webhook to dump messages to')
    parser.add_argument('--debug', help="Print lots of extra stuff for debugging", action='store_true')
    opts = parser.parse_args()

    config = configparser.RawConfigParser()
    config.read(opts.config)
    consumer_key = config.get("Twitter", "consumer_key")
    consumer_secret = config.get("Twitter", "consumer_secret")
    access_token = config.get("Twitter", "access_token")
    access_secret = config.get("Twitter", "access_secret")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)

    if opts.stream:
        stream_twitter(opts.userlist, webhook=opts.webhook, debug=opts.debug)

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
