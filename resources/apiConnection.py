'''
|--------------------------------------------------------------------------
| Importing packages and Twitter API keys:
|--------------------------------------------------------------------------
|
| We import our keys dictionaries with all our API keys. These should
| remain hidden i.e. Cannot be hardcoded as part of your controller.
|
| We also import tweepy allowing us to access the twitter api as well as
| authenticate our twitter user account and gain access to our twitter
| application.
|
|--------------------------------------------------------------------------
'''
import tweepy
from keyStorage.keys import keys

'''
|--------------------------------------------------------------------------
| Connect to twitter API:
|--------------------------------------------------------------------------
|
| Authenticates twitter account credentials, then connects to twitter 
| application, and finnaly returns tweepy access to twitter API. 
|
|--------------------------------------------------------------------------
'''
class apiConnect():
	'''
    |--------------------------------------------------------------------------
    | apiConnect docstring:
    |--------------------------------------------------------------------------
    |
    | Uses our secret keys to connect to a specific twitter application, thus
    | granting us access to it through the twitter API.
    |
	|--------------------------------------------------------------------------
	'''
	def __init__(self, **kwargs):
		self.__dict__.update(kwargs)

	# Authenticate user credentials and give access to twitter API
	def authentication(self):
		# Use user keys
		CONSUMER_KEY = keys['consumer_key']
		CONSUMER_SECRET = keys['consumer_secret']
		ACCESS_KEY = keys['access_token']
		ACCESS_SECRET = keys['access_token_secret']

		# Authenticate twitter account credentials using tweepy
		auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

		# Set access keys for authenticated user
		auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

		# Set twitter API through tweepy and return api
		api = tweepy.API(auth, retry_count=5, retry_errors=None, timeout=120, compression=False)
		return api