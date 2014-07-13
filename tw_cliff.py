#!/usr/bin/env python
import sys
import os

from cliff.app import App
from cliff.command import Command
from cliff.commandmanager import CommandManager

import twitterlib


# Base class for populating Twitter sub-commands with standard arguments.
class TwitterCommand(Command):
    "Base command to Twitter timeline sub-commands"

    def open_api(self, parsed_args):
        api = twitterlib.API(parsed_args.api_key, parsed_args.api_secret,
                             parsed_args.access_token,
                             parsed_args.access_secret)
        return api

    def get_parser(self, prog_name):
        parser = super(TwitterCommand, self).get_parser(prog_name)
        parser.add_argument('--api-key',
                            required='API_KEY' not in os.environ,
                            default=os.environ.get('API_KEY', None))
        parser.add_argument('--api-secret',
                            required='API_SECRET' not in os.environ,
                            default=os.environ.get('API_SECRET', None))
        parser.add_argument('--access-token',
                            required='ACCESS_TOKEN' not in os.environ,
                            default=os.environ.get('ACCESS_TOKEN', None))
        parser.add_argument('--access-secret',
                            required='ACCESS_SECRET' not in os.environ,
                            default=os.environ.get('ACCESS_SECRET', None))
        return parser


# Concrete classes that implemented TWitter sub-commands.
class Timeline(TwitterCommand):
    "Display recent tweets from users timeline"

    def take_action(self, parsed_args):
        api = self.open_api(parsed_args)
        for status in api.timeline:
            print u"%s: %s" % (status.user.screen_name, status.text)


class Mentions(TwitterCommand):
    "Display recent tweets mentioning user"

    def take_action(self, parsed_args):
        api = self.open_api(parsed_args)
        for status in api.mentions:
            print u"%s: %s" % (status.user.screen_name, status.text)


class Retweets(TwitterCommand):
    "Display recent retweets from user's timeline"

    def take_action(self, parsed_args):
        api = self.open_api(parsed_args)
        for status in api.retweets:
            print u"%s: %s" % (status.user.screen_name, status.text)


# Command manager and manual registration of sub-commands.
# Ordinarily registration would occur via setuptools entrypoints.
COMMAND_MANAGER = CommandManager('cliff.demo')
COMMAND_MANAGER.add_command('timeline', Timeline)
COMMAND_MANAGER.add_command('mentions', Mentions)
COMMAND_MANAGER.add_command('retweets', Retweets)


# Main application class.
class TwitterApp(App):

    def __init__(self):
        super(TwitterApp, self).__init__(
            description='Twitter command line application',
            version='0.1',
            command_manager=COMMAND_MANAGER,
        )


# Application needs to be run with command line to parse.
if __name__ == '__main__':
    app = TwitterApp()
    sys.exit(app.run(sys.argv[1:]))
