#!/usr/bin/env python

import json
from sys import argv


def replay_logs(logfile):
    lfile = open(logfile, 'r')

    for line in lfile:
        jblob = json.loads(line)
        print(jblob)

if __name__ == "__main__":
    if len(argv) == 2:
        replay_logs(argv[1])

    else:
        print("./replaylogs.py [LOGFILE]")
