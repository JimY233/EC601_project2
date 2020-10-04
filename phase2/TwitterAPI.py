import tweepy
import sys

def twitter_search(keyword,num):
    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

    #Please enter Twitter API credentials here
    #consumer_key = "Enter the consumer_key" 
    #consumer_secret = "Enter the consumer_secret"
    #access_key = "Enter the access_key"
    #access_secret = "Enter the access_secret"
     
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
     
    api = tweepy.API(auth)

    text = ""

    for tweet in tweepy.Cursor(api.search,q=keyword).items(num):
        text += tweet.text.translate(non_bmp_map)

    return text

if __name__ == '__main__':
    
    keyword = input("Please enter the keyword:\n")
    num = int(input("Please enter how many tweets you want to analyze:\n"))

    twitter_search(keyword,num)
    
