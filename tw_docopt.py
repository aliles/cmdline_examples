#!/usr/bin/env python
"""Minimal Twitter client

Command line Twitter client demonstrating use of docopt command line parsing
package.

Usage:
  tw_docopt.py [options] (timeline|mentions|retweets)
  tw_docopt.py -h | --help
  tw_docopt.py --version

Options:
  -h --help                 Show this screen.
  --version                 Show version.
  --api-key KEY             Twitter API key.
  --api-secret SECRET       Twitter API secert.
  --access-token TOKEN      Twitter client access token.
  --access-secret SECRET    Twitter client access secret.
"""
import os

from docopt import docopt

import twitterlib

# Maps command line flags to environment variables.
ENV_VARS = {
    '--api-key': 'API_KEY',
    '--api-secret': 'API_SECRET',
    '--access-token': 'ACCESS_TOKEN',
    '--access-secret': 'ACCESS_SECRET'
}


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
    arguments = docopt(__doc__, version="PyConAU 2014")
    # Update missing auth tokens from environment variables.
    for option in arguments:
        if option not in ENV_VARS:
            continue
        if arguments[option] is not None:
            continue
        arguments[option] = os.environ[ENV_VARS[option]]
    # Create Twitter API object.
    api = twitterlib.API(
        arguments['--api-key'],
        arguments['--api-secret'],
        arguments['--access-token'],
        arguments['--access-secret']
    )
    # Run chosen sub-command.
    for command in SUB_COMMANDS:
        if not arguments[command]:
            continue
        SUB_COMMANDS[command](api)
