#!/usr/bin/env python
import argparse
import os

import twitterlib


# Sub-commands for select Twitter feeds.
def timeline(args):
    "Display recent tweets from users timeline"
    api = twitterlib.API(args.api_key,
                         args.api_secret,
                         args.access_token,
                         args.access_secret)
    for status in api.timeline:
        print u"%s: %s" % (status.user.screen_name, status.text)


def mentions(args):
    "Display recent tweets mentioning user"
    api = twitterlib.API(args.api_key,
                         args.api_secret,
                         args.access_token,
                         args.access_secret)
    for status in api.mentions:
        print u"%s: %s" % (status.user.screen_name, status.text)


def retweets(args):
    "Display recent retweets from user's timeline"
    api = twitterlib.API(args.api_key,
                         args.api_secret,
                         args.access_token,
                         args.access_secret)
    for status in api.retweets:
        print u"%s: %s" % (status.user.screen_name, status.text)


# Process command line using argparse.
def parse_commandline(args=None):
    "Process command line using optparse"
    parser = argparse.ArgumentParser()
    parser.add_argument("--api-key",
                        required='API_KEY' not in os.environ,
                        default=os.environ.get('API_KEY', None))
    parser.add_argument("--api-secret",
                        required='API_SECRET' not in os.environ,
                        default=os.environ.get('API_SECRET', None))
    parser.add_argument("--access-token",
                        required='ACCESS_TOKEN' not in os.environ,
                        default=os.environ.get('ACCESS_TOKEN', None))
    parser.add_argument("--access-secret",
                        required='ACCESS_SECRET' not in os.environ,
                        default=os.environ.get('ACCESS_SECRET', None))
    # Create sub-parser and register sub-command funciton.
    subparsers = parser.add_subparsers(dest='sub_command')
    subparsers.add_parser('timeline').set_defaults(func=timeline)
    subparsers.add_parser('mentions').set_defaults(func=mentions)
    subparsers.add_parser('retweets').set_defaults(func=retweets)
    return parser.parse_args(args)

# Command line execution.
if __name__ == '__main__':
    args = parse_commandline()
    args.func(args)
