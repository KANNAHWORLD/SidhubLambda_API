import json
import requests


ARXIV_CLASSIFICATION_URL = "http://35.247.118.232:8000"
PING_REQUEST = {
    "statusCode": 200,
    "headers": {
        "Content-Type": "application/json"
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
        },
        'body': json.dumps(data)
    }

def handle_arxiv_classification(data):

    response = requests.post(ARXIV_CLASSIFICATION_URL, json={'data': data, 'resource': 'arxivClassification'})
    return response.json()

def handler(event, context):
    
    # return make_good_response({'event': event})

    if 'path' not in event:
        return make_good_response(PING_REQUEST)
    path = event['path']

    if path == '/Projects/arxivClassification' and event['body'] and 'data' in event['body']:
        
        query = json.loads(event['body'])['data']
        classification = handle_arxiv_classification(query)
        
        return make_good_response({
            'classification': classification
        })
        
    return PING_REQUEST


import logging
import time
if __name__ == "__main__":

    test_data = "What is the neural network and how does it work?"

    print(handle_arxiv_classification(test_data))
