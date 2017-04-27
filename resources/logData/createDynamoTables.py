'''
|--------------------------------------------------------------------------
| Importing packages:
|--------------------------------------------------------------------------
|
| Importing boto3 package, to easily access our DynamoDB account.
|
|--------------------------------------------------------------------------
'''
import boto3

'''
|--------------------------------------------------------------------------
| Database table creation:
|--------------------------------------------------------------------------
|
| Checks if a table with Table_name = 'follower' exists, under current 
| client profile. If table exists returns boolean = True. If table
| doesn't exist, creates new table with Table_name = 'followers'
| and returns boolean = False.
|
|--------------------------------------------------------------------------
'''
class tableCreate(object):
    '''
    |--------------------------------------------------------------------------
    | tableCreate docstring:
    |--------------------------------------------------------------------------
    |
    | Checks if follower table exists and creates table if it doesn't exist.
    |
    |--------------------------------------------------------------------------
    '''
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    # Query client and list_tables to see if table exists or not
    def queryCreate(self):
        # Instantiate your dynamo client object
        client = boto3.client('dynamodb')

        # Get an array of table names associated with the current account and endpoint.
        response = client.list_tables()

        if 'followers' in response['TableNames']:
            table_found = True
        else:
            table_found = False
            # Get the service resource.
            dynamodb = boto3.resource('dynamodb')

            # Create the DynamoDB table called followers
            table = dynamodb.create_table(
                TableName ='followers',
                KeySchema =
                [
                    {
                        'AttributeName': 'follower_id',
                        'KeyType': 'HASH'
                    }
                ],
                AttributeDefinitions =
                [
                    {
                        'AttributeName': 'follower_id',
                        'AttributeType': 'N'
                    }
                ],
                ProvisionedThroughput =
                {
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5
                }
            )

            # Wait until the table exists.
            table.meta.client.get_waiter('table_exists').wait(TableName='followers')

        return table_found