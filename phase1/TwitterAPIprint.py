import tweepy

import sys
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

consumer_key = "Enter the consumer_key" 
consumer_secret = "Enter the consumer_secret"
access_key = "Enter the access_key"
access_secret = "Enter the access_secret"
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)
 
public_tweets = api.user_timeline('LeoDiCaprio') //who’s tweets you want to record

i = 1 
for tweet in public_tweets:
    print (tweet.text.translate(non_bmp_map))
    i = i + 1
    if i == 10:
        break
