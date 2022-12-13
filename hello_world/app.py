import json


def lambda_handler(event, context):

    headers = {"Content-Type": "Application/json"}
    print('add it to see logs change  plesase ... !!')

    return {
        "headers": headers,
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello World, HOw are you ?",
        }),
    }
