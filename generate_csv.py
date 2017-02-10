from api.tweet import search
from helper.func import unique_csv
from textblob import TextBlob
import sys
import csv

topic = sys.argv[1] if len(sys.argv) >= 2 else ""


with open(unique_csv(topic, 'output'), 'w', newline = '\n') as f:

    writer = csv.DictWriter(f, fieldnames = ['Tweet', 'Sentiment'])
    writer.writeheader()

    for tweet in search(topic):
        text = TextBlob(tweet.text)
        sentiment = text.sentiment.polarity
        polarity = 'Positive' if sentiment >= 0 else 'Negative'
        writer.writerow({ 'Tweet': text, 'Sentiment': polarity })
