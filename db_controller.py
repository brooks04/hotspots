import json
import sqlite3
import random

def insertMeeting(content):
    con = sqlite3.connect('schedule.db')
    cur = con.cursor()

    if content['Method'] == 'Slack':
        cur.execute('SELECT * FROM People WHERE SlackID = ?', (content['Organizer']))
    elif content['Method'] == 'Phone':
        cur.execute('SELECT * FROM People WHERE PhoneNum = ?', (content['Organizer']))

    org = cur.fetch()

    cur.execute('INSERT INTO Schedule VALUES (?, ?, ?, ?)', (random.randrange(2000000), 1, content['Time'], content['requestTime']))
    con.commit()

def removeMeeting(id):
    con = sqlite3.connect('schedule.db')
    cur = con.cursor()

    cur.execute('DELETE FROM Schedule WHERE PersonID = ?', (id))