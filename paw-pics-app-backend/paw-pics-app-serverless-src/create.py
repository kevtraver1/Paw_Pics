import boto3
import uuid
import json
import flask
#establish connection to dynamodb
dynamodb_table = boto3.resource('dynamodb').Table("posts")

# get item
response = dynamodb_table.get_item(Key={'user_id': 'ktravers'})
print(response)