
import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(
    TableName='Great guitar albums',
    KeySchema=[
        {
            'AttributeName': 'album',
            "AttributeType": "S", # seting the type as a String
        },
        {
            'AttributeName': 'Band',
            "AttributeType": "S", # seting the type as a String
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'album',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'Band',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status:", table.table_status)
