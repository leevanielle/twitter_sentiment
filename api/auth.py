from .secrets import *
from tweepy import OAuthHandler

def verify():
    handler = OAuthHandler(consumer_key, consumer_secret)
    handler.set_access_token(access_token, access_token_secret)

    return handler
