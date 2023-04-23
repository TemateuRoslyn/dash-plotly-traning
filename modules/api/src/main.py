# app.py
from flask import Flask, jsonify, request
import json

# controllers
from controllers.accelerometre1_controller import *

# models
from models.accelerometre1 import Accelerometre1
from models.accelerometre2 import Accelerometre2


app = Flask(__name__)

acc1 =  Accelerometre1()
acc2 =  Accelerometre2()


@app.route('/', methods=['GET'])
def index():
    return "Welcome to this example api for dash plottly"

@app.route('/accelerometre1/next', methods=['GET'])
def get_accelerometre1():
    nextCapteurValue = acc1.get_next()
    return json.dumps(nextCapteurValue)

@app.route('/accelerometre2/next', methods=['GET'])
def get_accelerometre2():
    nextCapteurValue = acc2.get_next()
    return json.dumps(nextCapteurValue)


if __name__ == '__main__':
    app.run()

