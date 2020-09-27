Please read the report named EC601 project2 phase1.pdf. The code and results are showed there.

Considering the requirement that the keys should not be public, I only showed the code before I entered API key, API secret key, access token, access secret token. That is to say,
Please enter your API key, API secret key, access token, access secret token derived from the Twitter API Developer Portal to the code where:

consumer_key = "Enter the Consumer Key"  
consumer_secret = "Enter the consumer secret"  
access_key = "Enter the access key"  
access_secret = "Enter teh access secret"

It is important to use non_bmp_map when printing the tweet.text since some emoji can not be shown and cause error.

The code below would solve this problem:  
import sys  
non_bmp_map = dict.fromkeys(range(0x10000,sys.maxunicode+1),0xfffd)  
print(tweet.text.translate(non_bmp_map))

Remember to change the key word as you want. 
