from flask import Flask, jsonify
from flask_restful import Resource, Api
import requests

def task_func(api_url, template_folder):
    # Initialize the Flask application with the specified template folder
    app = Flask(__name__, template_folder=template_folder)
    
    # Initialize the Flask-RESTful API
    api = Api(app)
    
    # Define a Resource to handle requests to the endpoint
    class DataResource(Resource):
        def get(self):
            try:
                # Make a GET request to the external API
                response = requests.get(api_url)
                # Raise an exception if the request was unsuccessful
                response.raise_for_status()
                # Return the JSON response from the external API
                return jsonify(response.json())
            except requests.exceptions.RequestException as e:
                # Return an error message and status code if the request fails
                return {'error': str(e)}, 500
    
    # Add the resource to the API, accessible at the '/data' endpoint
    api.add_resource(DataResource, '/data')
    
    return app
