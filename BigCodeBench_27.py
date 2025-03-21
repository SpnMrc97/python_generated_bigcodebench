import json
import base64
from datetime import datetime

def task_func(data: dict, DATE_FORMAT="%Y-%m-%d %H:%M:%S") -> str:
    # Check if 'timestamp' key is already in data
    if 'timestamp' in data:
        raise ValueError("The input dictionary should not contain a key named 'timestamp'.")

    # Add current timestamp to the dictionary
    current_timestamp = datetime.now().strftime(DATE_FORMAT)
    data['timestamp'] = current_timestamp

    # Serialize the dictionary to a JSON-formatted string
    json_string = json.dumps(data)

    # Encode the JSON string using base64 with ASCII character encoding
    encoded_bytes = base64.b64encode(json_string.encode('ascii'))
    encoded_str = encoded_bytes.decode('ascii')

    return encoded_str
