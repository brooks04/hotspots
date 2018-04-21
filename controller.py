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

@app.route('/user', methods=['GET', 'POST'])
def user():
    content = request.get_json()
    print(type(content))

    if len(content.keys()) != 2 or 'username' not in content.keys() or 'password' not in content.keys():
        return jsonify({'Status' : 'BAD'})

    if verify(content['username'], content['password']):
        return jsonify({'Status' : 'OK'})

    return jsonify({'Status' : 'NF'})

def verify(username, password):
    con = sqlite3.connect('user_info.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM user_info WHERE username = ? AND password = ?', (username, password))
    if len(cur.fetchall()) != 0:
        return True
    else:
        return False

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)