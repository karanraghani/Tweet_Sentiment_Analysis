import tweepy
from textblob import TextBlob

consumer_key = 'sL4mmpX8SnNBtpjixopqKFdCU'
consumer_secret = 'EHemfzCIRkA6kZYK1RVOt83Zrx0czB23tjRiHhPEfAsPksMt4U'

access_token = '108255776-PtuSleGqM8nuV0xLeXI4g2rvzvrDBnd7dY9lHuV7'
access_token_secret = 'GNa0sm6lfCmrIcvbycSNKq57Jbu0HnFXQAeR1Us7c93qF'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Tesla')

#for tweet in public_tweets:
#	print (tweet)
#	analysis = TextBlob(tweet.text)
#	print (analysis.sentiment)

file_tweets = open('tweets_polarity.txt','w')

for tweet in public_tweets:	
	analysis = TextBlob(tweet.text)
	file_tweets.write(tweet.text+'\t')
	if analysis.sentiment.polarity > .01:
		file_tweets.write('Positive \n')
	else:
		file_tweets.write('Negative \n')


file_tweets.close()

