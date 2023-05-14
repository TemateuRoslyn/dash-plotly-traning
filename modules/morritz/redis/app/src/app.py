# app.py
from flask import Flask, jsonify, request
import redis
import json


# models
from accelerometre1 import Accelerometre1


app = Flask(__name__)
r = redis.Redis(host='172.20.0.2',port=6379)

acc1 =  Accelerometre1()


@app.route('/', methods=['GET'])
def index():
    print(r.ping())
    return 'welcome to our website'

@app.route('/accelerometre1/next', methods=['GET'])
def get_employees():
    nextCapteurValue = acc1.get_next()
    r.set('to','12345')
    print(r.get('to'))
    return json.dumps(nextCapteurValue)


if __name__ == '__main__':
    app.run(port=8000)

