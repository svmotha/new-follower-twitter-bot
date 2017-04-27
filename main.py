from __future__ import print_function
'''
|--------------------------------------------------------------------------
| Send direct messages to new followers on Twitter
|--------------------------------------------------------------------------
|
| 	  Author	|	Victor Motha
|   Copyright	|	2017
| 	Objective	|	Learning how to engage new twitter followers
| 	 License	|	MIT
|
|--------------------------------------------------------------------------
'''

'''
|--------------------------------------------------------------------------
| Importing packages:
|--------------------------------------------------------------------------
|
| We import our variables dictionaries with all global variables.
| 
| We also import our log, createDynamoTables and boto3 modules, allowing 
| us to easily access and interact with our server on DynamoDB.
|
|--------------------------------------------------------------------------
'''
from resources.apiConnection import apiConnect
from resources.logData import log, createDynamoTables
from resources.variables.variableKeys import variables
import boto3


'''
|--------------------------------------------------------------------------
| Responding To New Followers:
|--------------------------------------------------------------------------
|
| This is where we get a list of our followers and query through the DynamoDB
| to ensure we don't repeat Direct Messages (DMs) to new followers. To get 
| DM content, we will use our variables dictionary.
|
| Using tweepy we get follower details, such as the user id, screen
| name, whether we have sent the follower a follow request in return, etc.
| This is stored in our DynamoDB to allow for log querying. We finally
| use tweepy to send a DM to the new follower.
|
|--------------------------------------------------------------------------
'''
def handler(event, context):
	api = apiConnect().authentification()
	new_followers = api.followers()
	newDM = variables['direct_message_text']

	# Check if table exists and create it
	table_found = createDynamoTables.tableCreate().queryCreate()

	# Get the service resource.
	dynamodb = boto3.resource('dynamodb')

	'''
	|---------------------------------------------------------------------------
	| 
	| Instantiate a table resource object without actually creating a DynamoDB 
	| table. Note that the attributes of this table are lazy-loaded: a request
	| is not made nor are the attribute values populated until the attributes
	| on the table resource are accessed or its load() method is called.
	|
	|--------------------------------------------------------------------------
	'''
	table = dynamodb.Table('followers')
	
	if table_found == False:
		'''
		|---------------------------------------------------------------------------
		| 
		| Add last follower to DynamoDB. This ensures that the next time the 
		| script runs; it will only send direct messages to new followers 
		| from the time you first ran this script.
		|
		|--------------------------------------------------------------------------
		'''
		log.logCenter().dynamoPut(follower=new_followers[0], table=table)

		# Printing to cli for troubleshooting purposes
		print (variables['table_not_found'])

	else:
		# Iterate through latest followers and check for new followers
		for i, follower in enumerate(new_followers):
			log_query = log.logCenter().dynamoQuery(follower=new_followers[i], table=table)

			found_follower = isinstance(log_query, bool)
			if found_follower == False:
				# Printing to cli for troubleshooting purposes
				print (variables['no_new_followers'])
				# No new followers, thus break and end loop
				break
			else:
				# New follower - Add user to DynamoDB
				log.logCenter().dynamoPut(follower=new_followers[i], table=table)
				# Printing to cli for troubleshooting purposes
				print (variables['new_follower_found'])

				# Sending DM to User
				api.send_direct_message(user_id = follower.id, text = newDM)
				# Printing to cli for troubleshooting purposes
				print (variables['direct_message_sent_successfully'])