import json
import sqlite3
import random

def insertMeeting(content):
    con = sqlite3.connect('schedule.db')
    cur = con.cursor()

    if content['Method'] == 'Slack':
        print('Slack')
        cur.execute('SELECT * FROM People WHERE SlackID = ?', (content['Organizer'],))
    elif content['Method'] == 'Phone':
        print('Phone')
        cur.execute('SELECT * FROM People WHERE PhoneNum = ?', (content['Organizer'],))

    org = cur.fetchone()[0]
    scheduleID = random.randrange(2000000)
    cur.execute('INSERT INTO Schedule VALUES (?, ?, ?, ?, ?)', (scheduleID, 1, content['Time'], content['RequestTime'], org))
    idList = []
    for person in content['Members']:
        cur.execute('SELECT * FROM People WHERE Name LIKE ?', ('%' + person +'%',))
        idList.append(int(cur.fetchone()[0]))

    for pid in idList:
        cur.execute('INSERT INTO Notify VALUES (?, ?)', (scheduleID, pid))

    con.commit()

def removeMeeting(id):
    con = sqlite3.connect('schedule.db')
    cur = con.cursor()

    cur.execute('DELETE FROM Schedule WHERE PersonID = ?', (id))

def setRoom(content):
    con = sqlite3.connect('schedule.db')
    cur = con.cursor()
    
    print(content, type(content['id']), type(content['room']))
    personID = content['id']
    roomID = content['room']

    cur.execute('SELECT * FROM Schedule WHERE RoomID = ? AND PersonID = ?', (personID, roomID))
    data = cur.fetchall()
    if len(data) > 0:
        cur.execute('SELECT * FROM Rooms WHERE RoomID = ?', (roomID))
        data = cur.fetchone()[2] 
        if data == 0:
            cur.execute('UPDATE Rooms SET InUse = ? WHERE RoomID = ?', (1, RoomID))
        else:
            cur.execute('UPDATE Rooms SET InUse = ? WHERE RoomID = ?', (0, RoomID))


def readData():
    print('Reading Data')
    con = sqlite3.connect('schedule.db')
    cur = con.cursor()

    cur.execute('PRAGMA table_info(People)')
    dat = cur.fetchall()
    print(dat)
    cur.execute('SELECT * FROM People')
    dat = cur.fetchall()
    for row in dat:
        print(row)

    cur.execute('PRAGMA table_info(Rooms)')
    dat = cur.fetchall()
    print(dat)
    cur.execute('SELECT * FROM Rooms')
    dat = cur.fetchall()
    for row in dat:
        print(row)    

    cur.execute('PRAGMA table_info(Schedule)')
    dat = cur.fetchall()
    print(dat)
    cur.execute('SELECT * FROM Schedule')
    dat = cur.fetchall()
    for row in dat:
        print(row)

    cur.execute('PRAGMA table_info(Notify)')
    dat = cur.fetchall()
    print(dat)
    cur.execute('SELECT * FROM Notify')
    dat = cur.fetchall()
    for row in dat:
        print(row)