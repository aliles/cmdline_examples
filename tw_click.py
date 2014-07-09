#!/usr/bin/env python
import click

import twitterlib


# Main application defintion.
# Environment variables declared explicitly to allow no prefix to be applied.
@click.group()
@click.option('--api-key', envvar='API_KEY')
@click.option('--api-secret', envvar='API_SECRET')
@click.option('--access-token', envvar='ACCESS_TOKEN')
@click.option('--access-secret', envvar='ACCESS_SECRET')
@click.pass_context
def app(ctx, api_key, api_secret, access_token, access_secret):
    api = twitterlib.API(api_key, api_secret, access_token, access_secret)
    ctx.obj['API'] = api

# Sub-command definitions using command decorator from main program.
@app.command()
@click.pass_context
def timeline(ctx):
    "Display recent tweets from users timeline"
    for status in ctx.obj['API'].timeline:
        print u"%s: %s" % (status.user.screen_name, status.text)

@app.command()
@click.pass_context
def mentions(ctx):
    "Display recent tweets mentioning user"
    for status in ctx.obj['API'].mentions:
        print u"%s: %s" % (status.user.screen_name, status.text)

@app.command()
@click.pass_context
def retweets(ctx):
    "Display recent retweets from user's timeline"
    for status in ctx.obj['API'].retweets:
        print u"%s: %s" % (status.user.screen_name, status.text)

# Command line execution.
if __name__ == '__main__':
    app(obj={})
