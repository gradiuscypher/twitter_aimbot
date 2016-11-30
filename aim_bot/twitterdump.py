#!/usr/bin/env python

import twitter
import configparser
import json
import argparse


def stream_twitter(screen_name):
    user_id = t_client.users.lookup(screen_name=screen_name)[0]['id']

    stream = twitter.stream.TwitterStream(auth=auth, domain='stream.twitter.com')

    for message in stream.statuses.filter(follow=user_id):
        print(json.dumps(message))


def dump_twitter(screen_name, count=100, include_rts=0):
    tweets = t_client.statuses.user_timeline(include_rts=include_rts, screen_name=screen_name, count=count)
    for tweet in tweets:
        print(json.dumps(tweet))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="tcpdump style tool for twitter. can stream tweets or dump profiles")
    parser.add_argument('--dump', help='Dump a full twitter profile.', action='store_true')
    parser.add_argument('--stream', help='Dump a full twitter profile.', action='store_true')
    parser.add_argument('--retweets', help='Include retweets in a dump', action='store_true')
    parser.add_argument('-count', help='Number of tweets to pull down when dumping')
    parser.add_argument('config', help='Config file name')
    parser.add_argument('user', help="Target twitter user name")
    opts = parser.parse_args()

    config = configparser.RawConfigParser()
    config.read(opts.config)
    consumer_key = config.get("Twitter", "consumer_key")
    consumer_secret = config.get("Twitter", "consumer_secret")
    access_token = config.get("Twitter", "access_token")
    access_secret = config.get("Twitter", "access_secret")
    auth = twitter.OAuth(consumer_key=consumer_key, consumer_secret=consumer_secret, token=access_token,
                         token_secret=access_secret)
    t_client = twitter.Twitter(auth=auth)

    if opts.stream:
        stream_twitter(opts.user)

    if opts.dump:
        if opts.retweets:
            include_retweets = 1
        else:
            include_retweets = 0

        if opts.count is not None:
            dump_twitter(opts.user, count=opts.count, include_rts=include_retweets)
        else:
            dump_twitter(opts.user, include_rts=include_retweets)
