#!/usr/bin/env python

import json
import configparser
from sys import argv
from os import listdir
from importlib import import_module


class ReplayLogs:

    def __init__(self, config_file):
        config = configparser.RawConfigParser()
        config.read(config_file)
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
            visor.activate(event_message)

    def replay_logs(self, logfile):
        self.load_visors()
        lfile = open(logfile, 'r')

        for line in lfile:
            jblob = json.loads(line)
            self.evaluate_target(jblob)


if __name__ == "__main__":
    if len(argv) == 3:
        rl = ReplayLogs(argv[1])
        rl.replay_logs(argv[2])

    else:
        print("./replaylogs.py [CONFIG] [LOGFILE]")
