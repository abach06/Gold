import boto3 #import boto 3 module


dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('great_guitar_albums_Python') #var for table name

#delete item 
response = table.delete_item(
     Key={
        'album': 'Nevermind', 'artist': 'Nirvana'})  

print(response) #print response 
