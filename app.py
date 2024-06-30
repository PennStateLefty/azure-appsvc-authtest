from flask import Flask, request, jsonify
import os
import logging

app = Flask(__name__)

# Enable logging
logging.basicConfig(level=logging.INFO)

@app.route('/')
def show_auth_headers():
    try:
        logging.info('Received request')
        # List of Azure EasyAuth headers you are interested in
        auth_headers = [
            'X-MS-TOKEN-AAD-ID-TOKEN',
            'X-MS-CLIENT-PRINCIPAL-NAME',
            'X-MS-CLIENT-PRINCIPAL-ID'
        ]
        
        print(f"Received a request - logging to print command")

        # Capture and store these headers if they exist in the request
        captured_headers = {header: request.headers.get(header) for header in auth_headers if request.headers.get(header)}
        
        # Return the captured headers as a JSON response
        return jsonify(captured_headers)
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return jsonify({'error': 'An error occurred'})

if __name__ == '__main__':
    # Run the app on the port defined by the 'PORT' environment variable, or 5000 if not defined
    app.run(host="0.0.0.0", port=8000)