#!/usr/bin/env python
import begin

import twitterlib


@begin.subcommand
def timeline():
    "Display recent tweets from users timeline"
    for status in begin.context.api.timeline:
        print u"%s: %s" % (status.user.screen_name, status.text)

@begin.subcommand
def mentions():
    "Display recent tweets mentioning user"
    for status in begin.context.api.mentions:
        print u"%s: %s" % (status.user.screen_name, status.text)

@begin.subcommand
def retweets():
    "Display recent retweets from user's timeline"
    for status in begin.context.api.retweets:
        print u"%s: %s" % (status.user.screen_name, status.text)

@begin.start(env_prefix='')
def main(api_key='', api_secret='', access_token='', access_secret=''):
    """Minimal Twitter client

    Demonstrate the use of the begins command line application framework by
    implementing a simple Twitter command line client.
    """
    api = twitterlib.API(api_key, api_secret, access_token, access_secret)
    begin.context.api = api
