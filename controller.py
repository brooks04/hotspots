'''
                                                                
Authors: Beebkips

'''
import os
import json
import requests
import sqlite3
from flask import Flask, request, make_response, Response, jsonify
from db_controller import insertMeeting, removeMeeting

app = Flask(__name__)

@app.route('/')
def start():
    json = {'Status': 'UP'}
    return jsonify(json)

@app.route('/schedule', methods=['GET', 'POST'])
def schedule():
    content = request.get_json()
    return jsonify(content)

@app.route('/notify', methods=['GET'])
def notify():
    return jsonify({'Not' : 'Implemented'})

@app.route('/remove/<int:idnum>', methods=['POST'])
def remove(idnum):
    removeMeeting(idnum)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)