import json


def oi(event, context):
    body = {
        "message": "oi",
        "input": event,
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response


def tchau(event, context):
    body = {
        "message": "tchau",
        "input": event,
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response
