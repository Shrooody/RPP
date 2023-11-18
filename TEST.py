import requests
from flask import Flask, request, jsonify

url = 'http://127.0.0.1:5000/v1/add/region'

data = {'id': 1}

app = Flask(__name__)


@app.route('/v1/add/region', methods=['POST'])
def add_region():
    request.get_json()


response = requests.post(url, json=data)

print(response.status_code)
print(response.text)
