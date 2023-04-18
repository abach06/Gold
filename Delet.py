# Remove item from a DynamoDB table

import boto3

dynamodb = boto3.resource('dynamodb')
table_name = dynamodb.Table('great_guitar_albums')
response = table_name.delete_item(
    Key={
        'album':'Appetite for Destruction',
        'artist':'Guns n Roses'
    } 
)

print('Item successfully removed')
