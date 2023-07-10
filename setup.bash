#!/bin/bash

# Install the Flask and Boto3 dependencies.
pip install flask boto3

# Copy the app.py and index.html files to the current directory.
cp app.py index.html .

# Start the Flask application.
python app.run(host='0.0.0.0', port=8080)