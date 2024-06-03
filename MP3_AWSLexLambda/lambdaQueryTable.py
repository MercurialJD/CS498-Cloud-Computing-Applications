import json
import boto3
from collections import defaultdict


def alert(msg: str):
    print("+ ", end='')
    print(msg)


# Ref: https://gist.github.com/alexcasalboni/3ea2d8dda11c6b73bbf98adf2dd6a214#file-lex-py-L15
def load_session(event):
    current_slots = event['currentIntent']['slots']
    reservation = {
        'Source': current_slots['Source'],
        'Destination': current_slots['Destination']
    }

    session_attributes = event.get('sessionAttributes') or {}
    session_attributes['currentQuery'] = json.dumps(reservation)

    return session_attributes


# Ref: https://gist.github.com/alexcasalboni/3ea2d8dda11c6b73bbf98adf2dd6a214#file-lex-py-L15
def close(session_attributes, distance, fulfillment_state='Fulfilled'):
    response = {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': fulfillment_state,
            'message': {
                'contentType': 'PlainText',
                'content': distance,
            }
        }
    }

    return response


# Lambda handler
def lambda_handler(event, context):
    session_attributes = load_session(event)

    src, des = event['currentIntent']['slots']['Source'], event['currentIntent']['slots']['Destination']
    if src == des:
        alert("The {} and {} are the same!".format(src, des))
        return close(session_attributes, 0)

    # Getting the table
    dynamodb = boto3.resource('dynamodb')
    client = boto3.client('dynamodb')
    table = dynamodb.Table('MP3-Shortest-Distances')

    # Putting a try/catch to log to user when some error occurs
    try:
        db_response = table.get_item(
            Key = {
                    'Source': src,
                    'Destination': des
            }
        )

        # Check if exist the source-destination pair
        if 'Item' in db_response:
            dist = db_response['Item']['Distance']
            return close(session_attributes, int(dist))
        else:
            return close(session_attributes, -1)

    except Exception as e:
        alert(e)
        return {
            'statusCode': 400,
            'body': json.dumps('Error querying the table')
        }
