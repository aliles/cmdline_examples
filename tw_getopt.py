#!/usr/bin/env python
import getopt
import sys
import os

import twitterlib

# Maps command line flags to environment variables
ENV_VARS = {
    '--api-key': 'API_KEY',
    '--api-secret': 'API_SECRET',
    '--access-token': 'ACCESS_TOKEN',
    '--access-secret': 'ACCESS_SECRET'
}

# Process command line using getopt module
def parse_commandline(args=None):
    "Process command line using getopt"
    args = sys.argv[1:] if args is None else args
    optlist, args = getopt.gnu_getopt(sys.argv[1:], 'h', [
        'help', 'api-key=', 'api-secret=', 'access-token=', 'access-secret='
    ])
    opts = dict(optlist)
    if '-h' in opts or '--help' in opts:
        print "Minimal Twitter client Demonstrate the use of getopt"
        sys.exit(0)
    for flag in ENV_VARS:
        if flag in opts:
            continue
        opts[flag] = os.environ[ENV_VARS[flag]]
    return opts, args

# Sub-commands for select Twitter feeds
def timeline(api):
    "Display recent tweets from users timeline"
    for status in api.timeline:
        print u"%s: %s" % (status.user.screen_name, status.text)

def mentions(api):
    "Display recent tweets mentioning user"
    for status in api.mentions:
        print u"%s: %s" % (status.user.screen_name, status.text)

def retweets(api):
    "Display recent retweets from user's timeline"
    for status in api.retweets:
        print u"%s: %s" % (status.user.screen_name, status.text)

# Maps sub-command names to function calls
SUB_COMMANDS = {
    'timeline': timeline,
    'mentions': mentions,
    'retweets': retweets
}

# Command line execution
if __name__ == '__main__':
    opts, args = parse_commandline()
    api = twitterlib.API(
        opts['--api-key'],
        opts['--api-secret'],
        opts['--access-token'],
        opts['--access-secret']
    )
    SUB_COMMANDS[args[0]](api)
