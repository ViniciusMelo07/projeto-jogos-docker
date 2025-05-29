import urllib.request
import json
from datetime import datetime

def lambda_handler(event, context):
    cors_headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type"
    }

    if event.get("httpMethod") == "OPTIONS":
        return {
            "statusCode": 200,
            "headers": cors_headers,
            "body": json.dumps({"message": "CORS preflight OK"})
        }

    try:
        api_url = "http://SEU-IP-BACKEND:5000/report"
        with urllib.request.urlopen(api_url) as response:
            data = json.loads(response.read())

        return {
            "statusCode": 200,
            "headers": cors_headers,
            "body": json.dumps({
                "totalItems": len(data),
                "lastUpdate": datetime.utcnow().isoformat() + "Z"
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": cors_headers,
            "body": json.dumps({"error": str(e)})
        }
