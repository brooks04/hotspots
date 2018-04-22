'''
                                                                
Authors: Beebkips

'''
import os
import json
import requests
import sqlite3
from flask import Flask, request, make_response, Response, jsonify
from db_controller import insertMeeting, removeMeeting
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/')
def start():
    json = {'Status': 'UP'}
    return jsonify(json)

@app.route('/schedule', methods=['GET', 'POST'])
def schedule():
    content = request.get_json()
    print(content)
    return jsonify(content)

@app.route('/notify', methods=['GET'])
def notify():
    return jsonify({'Not' : 'Implemented'})

@app.route('/remove/<int:idnum>', methods=['POST'])
def remove(idnum):
    removeMeeting(idnum)

@app.route('/phone', methods=['GET', 'POST'])
def phone():
    number = request.form['From']
    message_body = request.form['Body']
    print(number, message_body)
    resp = MessagingResponse()
    msg_contents = message_body.split(" ")
    if (msg_contents[0].lower() == "schedule"):
        resp.message("How do I schedule stuff?")
    else:
        # Add a message
        resp.message("The Robots are coming! Head for the hills!")

    return str(resp)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)