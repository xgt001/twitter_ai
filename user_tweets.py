import tweepy
import webbrowser

consumer_key="kn72W8bE5hotLnYmrZ1xEw"
consumer_secret="DMlJCbLauL948xQHgwVx4gZOHW7QyKTuEGgCPWnjmg"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)


webbrowser.open(auth.get_authorization_url())


pin = raw_input('Enter your Verifier Pin').strip()


try:
    auth.get_access_token(verifier=pin)
except tweepy.TweepError:
    print 'Error! Failed to get access token.'

api = tweepy.API(auth)

print ("authentication success")
#the OAUTH Dance... dont replace the methods!

#foo = raw_input()

while(1):
    foo = raw_input()
    api.update_status(foo)
#tweet("#testing Twitter API's")