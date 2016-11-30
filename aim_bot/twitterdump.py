#!/usr/bin/env python

import twitter
import configparser
import json
import traceback
from sys import argv


def dump_stream(config_file, screen_name):
    config = configparser.RawConfigParser()
    config.read(config_file)
    consumer_key = config.get("Twitter", "consumer_key")
    consumer_secret = config.get("Twitter", "consumer_secret")
    access_token = config.get("Twitter", "access_token")
    access_secret = config.get("Twitter", "access_secret")
    debug = config.getboolean("Settings", "debug")
    auth = twitter.OAuth(consumer_key=consumer_key, consumer_secret=consumer_secret, token=access_token,
                         token_secret=access_secret)
    t_client = twitter.Twitter(auth=auth)

    # TODO: Extract the ID from this blob
    user_id = t_client.users.lookup(screen_name=screen_name)

    stream = twitter.stream.TwitterStream(auth=auth, domain='stream.twitter.com')

    # TODO: Do things with this
    for message in stream.statuses.filter(follow=user_id):
        print(message)

if __name__ == "__main__":
    dump_stream(argv[1], argv[2])
