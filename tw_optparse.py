#!/usr/bin/env python
from optparse import OptionParser
import os

import twitterlib


# Process command line using OptionParser.
def parse_commandline(args=None):
    "Process command line using optparse"
    parser = OptionParser()
    parser.add_option("--api-key",
                      default=os.environ.get('API_KEY', None))
    parser.add_option("--api-secret",
                      default=os.environ.get('API_SECRET', None))
    parser.add_option("--access-token",
                      default=os.environ.get('ACCESS_TOKEN', None))
    parser.add_option("--access-secret",
                      default=os.environ.get('ACCESS_SECRET', None))
    return parser.parse_args(args)


# Sub-commands for select Twitter feeds.
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


# Maps sub-command names to function calls.
SUB_COMMANDS = {
    'timeline': timeline,
    'mentions': mentions,
    'retweets': retweets
}

# Command line execution.
if __name__ == '__main__':
    opts, args = parse_commandline()
    api = twitterlib.API(
        opts.api_key,
        opts.api_secret,
        opts.access_token,
        opts.access_secret
    )
    SUB_COMMANDS[args[0]](api)
