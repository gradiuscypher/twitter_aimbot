#!/usr/bin/env python

import tweepy
import configparser
import pprint
import argparse
import requests


class StreamTweets(tweepy.StreamListener):
    def __init__(self, webhook):
        super().__init__()
        self.webhook = webhook

    def on_status(self, status):
        # TODO: can be replaced with chatbot alert library later when it is complete
        if self.webhook is not None:
            message_text = ""

            message_text += "**@" + status.user.screen_name + "**\n"
            message_text += status.text + "\n"

            requests.post(self.webhook, data={"content": message_text, "username": "Twitter Monitor"})
        else:
            pprint.pprint(repr(status))


def stream_twitter(username_list, webhook):
    userid_list = []

    for username in username_list:
        userid_list.append(str(api.get_user(username).id))

    tweet_listener = StreamTweets(webhook)
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
        stream_twitter(opts.userlist, webhook=opts.webhook)

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
