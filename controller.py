'''
                                                                
Authors: Beebkips

'''
import os
import json
import requests
import time
import sqlite3
from flask import Flask, request, make_response, Response, jsonify, render_template
from db_controller import insertMeeting, removeMeeting, readData, setRoom, getRoomStatus
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

app = Flask(__name__)

# Your Account SID from twilio.com/console
account_sid = "ACef85ef8fc339b4d9f2cc2269a8886773"
# Your Auth Token from twilio.com/console
auth_token  = "781e89ea329e82e4a3b0f8e116f2a2d1"

@app.route('/')
def start():
    json = {'Status': 'UP'}
    return jsonify(json)

@app.route('/home')
def home():
    return render_template('helper.html')

@app.route('/schedule', methods=['GET', 'POST'])
def schedule():
    content = request.get_json()
    print(content)
    resp = insertMeeting(content)

    client = Client(account_sid, auth_token)

    for number in resp[0]:
        message = client.messages.create(
        to="+1" + str(number), 
        from_="+14252233871",
        body="You have a meeting in room " + str(resp[1]) + " for " + str(resp[2]) + " mins")

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
    number = number[2:] #Removing the +1 from the start of the number
    message_body = request.form['Body']
    print(number, message_body)
    resp = MessagingResponse()
    msg_contents = message_body.split(" ")
    msg_length = len(msg_contents)
    if (msg_length > 0):
        task = msg_contents[0].lower()
        if (task == "schedule"):
            if (msg_length < 3):
                resp.message("For scheduling meetings, please use the format \"schedule <meeting length> <member1 member2 ...>\"")
            else:
                length = msg_contents[1]
                requestTime = time.time()
                members = msg_contents[2:]
                json = {"Method" : "Phone", "Organizer" : int(number), "Time" : int(length), "RequestTime" : int(requestTime), "Members" : members}
                insertMeeting(json)
                str1 = "Meeting queued! Length Requested = " + length + " Time of Request = " + str(int(requestTime)) + " Members = "
                for e in members:
                    str1 = str1 + e + ", "
                str1 = str1[:-2]
                resp.message(str1)
        elif (task == "remove"):
            usernum = number
            if (msg_length > 1):
                usernum = msg_contents[1]
            removeMeeting(usernum)
            resp.message("Meeting removed for user id " + usernum)
        else:
            resp.message(task + " is not a recognized command.")
    else:
        # Add a message
        resp.message("The Robots are coming! Head for the hills!")

    return str(resp)

@app.route('/read')
def read():
    readData()
    return jsonify({'Status' : 'Read'})

@app.route('/checkin',  methods=['GET', 'POST'])
def checkin():
    content = request.get_json()
    setRoom(content)
    return jsonify(content)

@app.route('/rooms', methods=['GET'])
def rooms():
    content = getRoomStatus()
    return jsonify(content)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)