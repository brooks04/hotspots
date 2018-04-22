import sqlite3

def start():
    con = sqlite3.connect('schedule.db')
    cur = con.cursor()

    try:
        # create rooms table
        cur.execute('CREATE TABLE Rooms(\
            ID INTEGER PRIMARY KEY, \
            Name TEXT NOT NULL, \
            Occupancy INTEGER, \
            InUse INTEGER)')

        # create people table
        cur.execute('CREATE TABLE People(\
            ID TEXT PRIMARY KEY, \
            PhoneNum INTEGER UNIQUE NOT NULL, \
            SlackID TEXT UNIQUE NOT NULL, \
            Name TEXT NOT NULL)')

        # create schedule table
        cur.execute('CREATE TABLE Schedule(\
            ID INTEGER PRIMARY KEY, \
            RoomID INTEGER, \
            Time INTEGER NOT NULL, \
            RequestTime INTEGER NOT NULL, \
            PersonID INTEGER, \
            FOREIGN KEY (RoomID) REFERENCES Rooms(ID))')

        # create notify table
        cur.execute('CREATE TABLE Notify( \
            ScheduleID INTEGER, \
            PersonID INTEGER, \
            FOREIGN KEY (ScheduleID) REFERENCES Schedule(ID) \
            FOREIGN KEY (PersonID) REFERENCES People(ID))')

        # commit changes
        con.commit()
        con.close()

        print('Good')

    except sqlite3.Error:
        # oh no
        print('oh no')

start()