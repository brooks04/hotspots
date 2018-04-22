import json
import sqlite3
import random

def insertMeeting(content):
    con = sqlite3.connect('schedule.db')
    cur = con.cursor()

    if content['Method'] == 'Slack':
        cur.execute('SELECT * FROM People WHERE SlackID = ?', (content['Organizer'],))
    elif content['Method'] == 'Phone':
        cur.execute('SELECT * FROM People WHERE PhoneNum = ?', (content['Organizer'],))

    org = cur.fetchone()[0]
    scheduleID = random.randrange(2000000)
    cur.execute('INSERT INTO Schedule VALUES (?, ?, ?, ?, ?)', (scheduleID, 1, content['Time'], content['RequestTime'], org))
    idList = []
    for person in content['Members']:
        cur.execute('SELECT * FROM People WHERE Name LIKE ?', ('%' + person +'%'))
        idList.append(cur.fetchone())

    for pid in idList:
        cur.execute('INSERT INTO Notify VALUES (?, ?)', (scheduleID, person))

    con.commit()

def removeMeeting(id):
    con = sqlite3.connect('schedule.db')
    cur = con.cursor()

    cur.execute('DELETE FROM Schedule WHERE PersonID = ?', (id))

def readData():
    print('Reading Data')
    con = sqlite3.connect('schedule.db')
    cur = con.cursor()

    cur.execute('SELECT * FROM People')
    dat = cur.fetchall()
    for row in dat:
        print(row)

    cur.execute('SELECT * FROM Rooms')
    dat = cur.fetchall()
    for row in dat:
        print(row)    

    cur.execute('SELECT * FROM Schedule')
    dat = cur.fetchall()
    for row in dat:
        print(row)

    cur.execute('SELECT * FROM Notify')
    dat = cur.fetchall()
    for row in dat:
        print(row)