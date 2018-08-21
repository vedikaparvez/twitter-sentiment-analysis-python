import tweepy
from textblob import TextBlob
import csv

consumer_key = "t0U0lP5o50wOeJpa2fyzfkzZW"
consumer_secret = "Zl6o92NvY3cSAvPbiN93Nv2Z8yvfKNio1kxT1knmeLESjRY3Zp"

access_token = "1024154522258558976-HnKsG6mmFpga0GX6688JYCSxumAfle"
access_token_secret = "1ksopwEp1gHL6oIETrGWP5pVZwJBgW8u1Xddwe7Ky6VGG"

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
