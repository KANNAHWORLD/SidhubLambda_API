import json
import requests


COMPUTE_ENGINE_URL = "http://34.82.168.208:8000"
PING_REQUEST = {
    "statusCode": 200,
    "headers": {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin' : '*',
        'Access-Control-Allow-Headers':'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
        'Access-Control-Allow-Credentials' : True,
    },
    "body": json.dumps({
        "message": "Hello from Lambda!"
    })
}


def make_good_response(data):
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin' : "*",
            'Access-Control-Allow-Methods': 'OPTIONS, POST, GET',
            'Access-Control-Allow-Headers':'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
            'Access-Control-Allow-Credentials' : True,
        },
        'body': json.dumps(data)
    }

def handle_arxiv_classification(data):

    response = requests.post(COMPUTE_ENGINE_URL, 
                            json={'data': data, 'resource': 'arxivClassification'}
                            )
    return response.json()

def handle_360_piazza_database(data):
    response = requests.post(COMPUTE_ENGINE_URL, 
                            json={'data': data, 'resource': '360PiazzaDatabase'}
                            )
    return response.json()

def handler(event, context):

    if 'path' not in event:
        return make_good_response(PING_REQUEST)
    
    path = event['path']

    if path == '/Projects/arxivClassification' and event['body'] and 'data' in event['body']:
                
        query = json.loads(event['body'])['data']
        classification = handle_arxiv_classification(query)
        
        return make_good_response(
        {
            'classification': classification['message'],
        })

    if path == '/Projects/360PiazzaDatabase' and event['body'] and 'data' in event['body']:
        query = json.loads(event['body'])['data']
        json_response = handle_360_piazza_database(query)
        return make_good_response({
            'database_response': json_response
        })
        
    return PING_REQUEST


import logging
import time
if __name__ == "__main__":

    test_data = "What is the neural network and how does it work?"

    print(handle_arxiv_classification(test_data))
