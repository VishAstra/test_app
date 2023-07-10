# app.py

import os
import boto3
from flask import Flask, render_template, request

app = Flask(__name__)

s3 = boto3.resource('s3', region_name='us-east-1')
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('DemoTable')

@app.route('/', methods=['GET', 'POST'])
def upload_photo():
    if request.method == 'GET':
        return render_template('index.html')

    name = request.form['name']
    age = request.form['age']
    photo = request.files['photo']

    thumbnail = photo.resize((100, 100))
    thumbnail_name = 'thumbnail_' + photo.filename
    s3.Bucket('vishathira').put_object_from_file(thumbnail, thumbnail_name)

    item = {
        'name': name,
        'age': age,
        'thumbnail': thumbnail_name
    }
    table.put_item(Item=item)

    return render_template('index.html', success=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)