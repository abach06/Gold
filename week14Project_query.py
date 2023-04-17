import boto3 

#importing key ***You will recieve error if not imported
from boto3.dynamodb.conditions import Key 


dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('great_guitar_albums') #var for table name

response = table.query( 
  KeyConditionExpression=Key('album').eq('Nevermind')   #query for items with "album"
)

print(response["Items"])
