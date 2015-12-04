from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from StringIO import StringIO
import simplejson
import json
import pprint


#please note that the keys are alterred use your own key values
consumer_key="kn72W8bE5hotLnYmrZadfa1xEw"
consumer_secret="DMlJCbLauL948xQHgwVx4gZOHW7QyKfdsTuEGgCPWnjmg"

access_token="221800045-9QxypqSWiCUa2adsfas715DrDIhbDlmGw0nJFIjUYG1AhF"
access_token_secret="5IakLqoBEMPc9p8aYFVasdfaaS0EjM5PfN6Ztv0yswtxgDto"

#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)
global count 

class StdOutListener(StreamListener):
	""" A listener handles tweets are the received from the stream. 
	This is a basic listener that just prints received tweets to stdout.

	"""
	
	def on_data(self, data):
		tweetk = simplejson.loads(data)
		tweets = []
		

		text = tweetk["text"].lower()


		if text.find("rt ") > -1:
			return
		tweets.append(text)

		
		print tweets
		
		count = 0

#		if (count == 10):
#			print "10 tweets fetched"
#			return False 


#		count = count + 1


		#print data
		return True

	def on_error(self, status):
		print status

if __name__ == '__main__':
	l = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	stream = Stream(auth, l)	
	
	stream.filter(languages=['en'],track=['ipl','leone'])


