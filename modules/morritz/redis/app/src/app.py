# app.py
from flask import Flask, jsonify, request
import json


# models
from accelerometre1 import Accelerometre1


app = Flask(__name__)

acc1 =  Accelerometre1()


@app.route('/', methods=['GET'])
def index():
    return "Welcome to this example api for dash plottly"

@app.route('/accelerometre1/next', methods=['GET'])
def get_employees():
    nextCapteurValue = acc1.get_next()
    return json.dumps(nextCapteurValue)


if __name__ == '__main__':
    app.run(port=8000)

