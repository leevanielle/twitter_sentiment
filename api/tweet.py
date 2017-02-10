from tweepy import API
from .auth import verify

api = API(verify())
search = lambda text: api.search(text)
