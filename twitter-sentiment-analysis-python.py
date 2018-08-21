import tweepy
from textblob import TextBlob
import csv

consumer_key = ""
consumer_secret = ""

access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search("Trump")

csvfile = "/Users/vedikaparvez/Desktop/twitter-sentiment-output.csv"

with open(csvfile,"w") as output:
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(["Tweet","Polarity","Subjectivity"])
    for tweet in public_tweets:
        writer.writerow([tweet.text.encode('utf-8').strip(),TextBlob(tweet.text).polarity,TextBlob(tweet.text).subjectivity])
