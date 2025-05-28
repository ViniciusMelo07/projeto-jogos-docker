import json
import requests
from datetime import datetime

def lambda_handler(event, context):
    try:
        api_url = "http://3.85.159.167:5000/report"
        response = requests.get(api_url)
        response.raise_for_status()
        
        data = response.json()

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "totalItems": len(data),
                "lastUpdate": datetime.utcnow().isoformat() + "Z"
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }
