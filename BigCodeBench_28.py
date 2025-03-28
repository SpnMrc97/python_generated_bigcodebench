import requests
import json
import base64

def task_func(data, url="http://your-api-url.com"):
    
    # Convert the dictionary to a JSON-formatted string
    json_data = json.dumps(data)
    
    # Encode the JSON string in base64
    base64_encoded = base64.b64encode(json_data.encode('utf-8')).decode('utf-8')
    
    # Prepare the payload for the POST request
    payload = {'payload': base64_encoded}
    
    # Send the POST request
    response = requests.post(url, json=payload)
    
    # Return the response object
    return response
