import json
import os
from botocore.vendored import requests

def lambda_handler(event,context):
    telegram_msg = event.get("message").get("text")

    chat_id = os.environ['CHAT_ID']
    telegram_token = os.environ['TELEGRAM_TOKEN']

    api_url = f"https://api.telegram.org/bot{telegram_token}/"

    params = {'chat_id': chat_id, 'text': telegram_msg}
    res = requests.post(f"{api_url}sendMessage", data = params).json()

    if res["ok"]:
        return {
            'statusCode': 200,
            'body': res['result']
        }
    else: 
        print(res)
        return {
            'statusCode': 400,
            'body': res
        }

"""

json event to test: 

{
    "update_id": 1234,
    "message": {
        "message_id": 1,
        "from": {
            "id": "@AO_Salutation_Bot",
            "is_bot": false,
            "first_name": "Alfonso",
            "last_name": "Osorio",
            "username":  "alfo",
            "language_code": "en"
        },
        "chat": {
            "id": 1234,
            "first_name": "Alfonso",
            "last_name": "Osorio",
            "username": "alfo",
            "type": "private"
        },
        "date": 1601136815,
        "text": "Hellooo there!!! API GW",
        "entities": [
            {
                "offset": 0,
                "length": 6,
                "type": "bot_command"
            }
        ]
    }
}



"""