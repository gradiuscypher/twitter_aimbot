#!/usr/bin/env python

import twitter
import configparser
import json
import traceback
from sys import argv
from os import listdir
from importlib import import_module


class Aimbot:

    def __init__(self, config_file):
        self.config = configparser.RawConfigParser()
        self.config.read(config_file)
        consumer_key = self.config.get("Twitter", "consumer_key")
        consumer_secret = self.config.get("Twitter", "consumer_secret")
        access_token = self.config.get("Twitter", "access_token")
        access_secret = self.config.get("Twitter", "access_secret")
        self.debug = self.config.getboolean("Settings", "debug")
        self.auth = twitter.OAuth(consumer_key=consumer_key, consumer_secret=consumer_secret, token=access_token,
                                  token_secret=access_secret)
        self.t_client = twitter.Twitter(auth=self.auth)
        self.loaded_visors = []
        self.visor_dir = 'tactical_visors_active'

    def load_visors(self):
        visor_count = 0

        for file_name in listdir(self.visor_dir):
            if not file_name.startswith('_') and file_name.endswith('.py'):
                module_name = file_name.replace('.py', '')
                self.loaded_visors.append(import_module(self.visor_dir + '.' + module_name))
                print("Tactical Visor Activated: [{}]".format(file_name))
                visor_count += 1
        print("You have {} Tactical Visors activated.".format(visor_count))

    def evaluate_target(self, event_message):
        for visor in self.loaded_visors:
            visor.activate(event_message, self.config, self.t_client)

    def visor_loop(self):
        self.load_visors()

        stream = twitter.stream.TwitterStream(auth=self.auth, domain='userstream.twitter.com')

        try:
            for message in stream.user():
                if self.debug:
                    message_string = json.dumps(message)
                    log_file = open("event_dump.log", 'a')
                    log_file.write(message_string + "\n")
                    log_file.close()

                self.evaluate_target(message)
        except:
            print(traceback.format_exc())

if __name__ == "__main__":
    if len(argv) == 2:
        ab = Aimbot(argv[1])
        ab.visor_loop()
    else:
        print("Command format:\n./aimbot.py [CONFIG]")
