from flask import Flask, request, jsonify, abort, render_template
import json
import requests

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    print('data', data)
    name = data['name']
    if name:
        return jsonify({'Message': 'Email sent successfully'})
    return jsonify({'Error': 'Failed, Try again'})

@app.route('/home', methods=['POST'])
def home():
    data = request.get_json()
    print(data)
    return jsonify({"name": data['data']})

import datetime
date_time = datetime.datetime.now()
print(date_time)
time_stamp = date_time.strftime("%d-%m-%Y %H:%M:%S")
print(time_stamp)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8081, debug=True)
