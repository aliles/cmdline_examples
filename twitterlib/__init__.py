"""Minimal Twitter API wrapping tweepy library."""
import tweepy


class API(object):

    def __init__(self, api_key, api_secret, access_token, access_secret):
        self.auth = tweepy.auth.OAuthHandler(api_key, api_secret)
        self.auth.set_access_token(access_token, access_secret)
        self.api = tweepy.API(self.auth)

    @property
    def request_limits(self):
        return self.api.rate_limit_status()

    @property
    def timeline(self):
        return self.api.home_timeline()

    @property
    def mentions(self):
        return self.api.mentions_timeline()

    @property
    def retweets(self):
        return self.api.retweets_of_me()


if __name__ == '__main__':
    import sys
    api = API(*sys.argv[1:5])
    print ' timeline '.center(72, '*')
    for status in api.timeline:
        print u"%s: %s" % (status.user.screen_name, status.text)
    print ' mentions '.center(72, '*')
    for status in api.mentions:
        print u"%s: %s" % (status.user.screen_name, status.text)
    print ' retweets '.center(72, '*')
    for status in api.retweets:
        print u"%s: %s" % (status.user.screen_name, status.text)
