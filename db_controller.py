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
    numbers = []
    for person in content['Members']:
        cur.execute('SELECT * FROM People WHERE Name LIKE ?', ('%' + person +'%',))
        row = cur.fetchone()
        idList.append(int(row[0]))
        numbers.append(row[1])

    for pid in idList:
        cur.execute('INSERT INTO Notify VALUES (?, ?)', (scheduleID, pid))

    con.commit()
    return numbers, 1, content['Time']

def removeMeeting(id):
    con = sqlite3.connect('schedule.db')
    cur = con.cursor()

    cur.execute('DELETE FROM Schedule WHERE PersonID = ?', (id))
    con.commit()

def setRoom(content):
    con = sqlite3.connect('schedule.db')
    cur = con.cursor()

    print(content, type(content['id']), type(content['room']))
    personID = content['id']
    roomID = content['room']

    checkedIn = False

    cur.execute('SELECT * FROM Schedule WHERE RoomID = ? AND PersonID = ?', (roomID, personID))
    data = cur.fetchall()
    if len(data) > 0:
        cur.execute('SELECT * FROM Rooms WHERE ID = ?', (roomID,))
        data = cur.fetchone()[2] 
        if data == 0:
            cur.execute('UPDATE Rooms SET InUse = ? WHERE ID = ?', (1, roomID))
        else:
            cur.execute('UPDATE Rooms SET InUse = ? WHERE ID = ?', (0, roomID))

    con.commit()

def getRoomStatus():
    con = sqlite3.connect('schedule.db')
    cur = con.cursor()

    cur.execute('SELECT * FROM Rooms')
    data = cur.fetchall()

    content = {}
    for row in data:
        content[row[0]] = row[2]

    return content

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