'''
                                                                
Authors: Beebkips

'''
import os
import json
import requests
import sqlite3
from flask import Flask, request, make_response, Response, jsonify
from db_controller import insertMeeting, removeMeeting, readData
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
    insertMeeting(content)
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
    msg_length = len(msg_contents)
    if (msg_length > 0 and msg_contents[0].lower() == "schedule"):
        if (msg_length < 4):
            resp.message("For scheduling meetings, please use the format \"schedule <time> <meeting length> <member1 member2 ...>\"")
        else:
            time = msg_contents[1]
            requestTime = msg_contents[2]
            members = msg_contents[3:]
            json = {"Method" : "Phone", "Organizer" : number, "Time" : time, "requestTime" : requestTime, "Members" : members}
            insertMeeting(json)
            str1 = "Meeting scheduled! Time = " + time + " Length = " + requestTime + " Members = "
            for e in members:
                str1 = str1 + e + ", "
            str1 = str1[:-2]
            resp.message(str1)
            
        #resp.message("How do I schedule stuff?")
    else:
        # Add a message
        resp.message("The Robots are coming! Head for the hills!")

    return str(resp)

@app.route('/read')
def read():
    readData()
    return jsonify({'Status' : 'Read'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)