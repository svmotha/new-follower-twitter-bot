'''
|--------------------------------------------------------------------------
| Importing packages:
|--------------------------------------------------------------------------
|
| Importing boto3.dynamodb.conditions.key package; to conditionally access 
| our DynamoDB tables using hash keys. Usually useful for querying tables
| in an efficient manner.
|
|--------------------------------------------------------------------------
'''
from boto3.dynamodb.conditions import Key

'''
|--------------------------------------------------------------------------
| Database log management controller:
|--------------------------------------------------------------------------
|
| Queries DynamoDB and updates list of new follwers who have been sent
| direct messages. Uses conditions module to improve DB querying.
|
|--------------------------------------------------------------------------
'''
class logCenter(object):
	'''
    |--------------------------------------------------------------------------
    | logCenter docstring:
    |--------------------------------------------------------------------------
    |
    | Queries and updates follwer table to keep track of followers you've
    | already sent direct messages to.
    |
	|--------------------------------------------------------------------------
	'''
	def __init__(self, **kwargs):
		self.__dict__.update(kwargs)

	# Update new followers to database (have already recieved direct messages)
	def dynamoPut(self, follower, table):
		table.put_item(
		   Item =
		   {
		        'follower_id': follower.id,
		        'screen_name': follower.screen_name,
		    }
		)
		return True

	# Query database to check if follower is new or not
	def dynamoQuery(self, follower, table):
		response = table.query(
		    KeyConditionExpression=Key('follower_id').eq(follower.id)
		)
		items = response['Items']
		if len(items) == 1:
			found = True
			return found, items
		else:
			found = False
			return found

