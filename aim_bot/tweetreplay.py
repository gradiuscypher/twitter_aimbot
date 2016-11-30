#!/usr/bin/env python

import json
import configparser
import twitter
import argparse
from os import listdir
from importlib import import_module


class ReplayLogs:

    def __init__(self, config_file):
        self.config = configparser.RawConfigParser()
        self.config.read(config_file)
        self.loaded_visors = []
        self.visor_dir = 'tactical_visors_active'
        consumer_key = self.config.get("Twitter", "consumer_key")
        consumer_secret = self.config.get("Twitter", "consumer_secret")
        access_token = self.config.get("Twitter", "access_token")
        access_secret = self.config.get("Twitter", "access_secret")
        self.auth = twitter.OAuth(consumer_key=consumer_key, consumer_secret=consumer_secret, token=access_token,
                                  token_secret=access_secret)
        self.t_client = twitter.Twitter(auth=self.auth)

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

    def replay_logs(self, logfile):
        self.load_visors()
        lfile = open(logfile, 'r')

        for line in lfile:
            jblob = json.loads(line)
            self.evaluate_target(jblob)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="tcpreplay style twitter tool. replays packets into the configured visors.")
    parser.add_argument('config', help='Config file name')
    parser.add_argument('logfile', help='Logfile to replay from')
    opts = parser.parse_args()

    rl = ReplayLogs(opts.config)
    rl.replay_logs(opts.logfile)
