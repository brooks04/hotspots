'''
                                                                
Authors: Beebkips

'''
import os
import json
import requests
import sqlite3
from flask import Flask, request, make_response, Response, jsonify

app = Flask(__name__)

@app.route('/')
def start():
    json = {'Status': 'UP'}
    return jsonify(json)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)