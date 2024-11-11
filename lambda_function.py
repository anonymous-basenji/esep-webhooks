import json
import os
import requests

def lambda_handler(event, context):
    # Deserialize input from json
    json_data = json.loads(event)

    # Create payload with issue URL
    payload = { 
        "text": f"Issue created: {json_data['issue']['html_url']}"
    }

    # Get Slack webhook URL from environment vars
    slack_url = os.getenv("SLACK_URL")
    
    # Send POST request to Slack webhook
    response = requests.post(slack_url, json=payload)

    # Return response content
    return response.text