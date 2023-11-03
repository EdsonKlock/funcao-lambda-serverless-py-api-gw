import json

def feriado(event, context):
    body = {
        "message": "feriado",
        "input": event,
        
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response