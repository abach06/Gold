
import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(
    TableName='great_guitar_albums',
    KeySchema=[
        {
            'AttributeName': 'album',
           'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'artist',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'album',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'artist',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status:", table.table_status)
