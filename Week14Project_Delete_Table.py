
# Delete a DynamoDB table

import boto3

dynamodb = boto3.client('dynamodb')

response = dynamodb.delete_table(
    TableName="great_guitar_albums",
)

print("Table successfully deleted")