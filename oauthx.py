import tweepy

#sha = raw_input()

k = []


# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

consumer_key="kn72W8bE5hotLnYmrZ1xEw"
consumer_secret="DMlJCbLauL948xQHgwVx4gZOHW7QyKTuEGgCPWnjmg"

access_token="221800045-9QxypqSWiCUa2715DrDIhbDlmGw0nJFIjUYG1AhF"
access_token_secret="5IakLqoBEMPc9p8aYFVaS0EjM5PfN6Ztv0yswtxgDto"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

print ("authentication success")
#the OAUTH Dance... dont replace the methods!

#foo = raw_input()
def tweet(status):
    '''
    updates the status of my twitter account
    requires tweepy (https://github.com/joshthecoder/tweepy)
    '''
    if len(status) > 140:
        raise Exception('status message is too long!')
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    result = api.update_status(status)
    return result


#api.update_status("openstack workshop")
tweet("#testing Twitter API's")

for karn in api.search("ipl"):
	print karn.text

	
