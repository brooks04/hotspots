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

    # org = cur.fetch()
    scheduleID = random.randrange(2000000)
    cur.execute('INSERT INTO Schedule VALUES (?, ?, ?, ?)', (scheduleID, 1, content['Time'], content['requestTime']))
    for person in content['members']:
        cur.execute('INSERT INTO Schedule VALUES (?, ?)', (scheduleID, person))
    #if content['Members'][0] == 'team':        
    #    cur.execute('INSERT INTO Schedule VALUES (?, ?)', (scheduleID, 1))
    #    cur.execute('INSERT INTO Schedule VALUES (?, ?)', (scheduleID, 2))
    #    cur.execute('INSERT INTO Schedule VALUES (?, ?)', (scheduleID, 3))
    #    cur.execute('INSERT INTO Schedule VALUES (?, ?)', (scheduleID, 4))
    #    cur.execute('INSERT INTO Schedule VALUES (?, ?)', (scheduleID, 5))


    con.commit()

def removeMeeting(id):
    con = sqlite3.connect('schedule.db')
    cur = con.cursor()

    cur.execute('DELETE FROM Schedule WHERE PersonID = ?', (id))

def readData():
    print('Reading Data')
    con = sqlite3.connect('schedule.db')
    cur = con.cursor()

    cur.execute('SELECT * FROM Schedule')
    dat = cur.fetchall()
    for row in dat:
        print(row)

    cur.execute('SELECT * FROM Notify')
    dat = cur.fetchall()
    for row in dat:
        print(row)