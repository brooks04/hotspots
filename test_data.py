import sqlite3

def start():
    con = sqlite3.connect('schedule.db')
    cur = con.cursor()

    try:
        # create rooms table
        # cur.execute('CREATE TABLE Rooms(ID INTEGER PRIMARY KEY, Name TEXT NOT NULL)')
        cur.execute('INSERT INTO Rooms VALUES(?, ?)', ('1', 'Room 1'))
        cur.execute('INSERT INTO Rooms VALUES(?, ?)', ('2', 'Room 2'))
        cur.execute('INSERT INTO Rooms VALUES(?, ?)', ('3', 'Room 3'))
        cur.execute('INSERT INTO Rooms VALUES(?, ?)', ('4', 'Room 4'))

        # create people table
        # cur.execute('CREATE TABLE People(ID TEXT PRIMARY KEY, PhoneNum INTEGER UNIQUE NOT NULL, SlackID TEXT UNIQUE NOT NULL, Name TEXT NOT NULL)')
        cur.execute('INSERT INTO People VALUES(?, ?, ?, ?)', ('1', '2532495291', 'UABV18PFZ', 'Brooke Stevenson'))
        cur.execute('INSERT INTO People VALUES(?, ?, ?, ?)', ('2', '2064035739', 'UAALNJ6LU', 'Conor Marsten'))
        cur.execute('INSERT INTO People VALUES(?, ?, ?, ?)', ('3', '2537651034', 'UABV4R4DV', 'Alex Reid'))
        cur.execute('INSERT INTO People VALUES(?, ?, ?, ?)', ('4', '2145168410', 'UAASGJRRB', 'Tej Gidvani'))
        cur.execute('INSERT INTO People VALUES(?, ?, ?, ?)', ('5', '2538864895', 'UAA76JDCG', 'Alvin Nguyen'))

        # create schedule table
        # cur.execute('CREATE TABLE Schedule(\
        #     ID INTEGER PRIMARY KEY, \
        #     RoomID INTEGER, \
        #     Time INTEGER NOT NULL, \
        #     RequestTime INTEGER NOT NULL, \
        #     PersonID INTEGER, \
        #     FOREIGN KEY (RoomID) REFERENCES Rooms(ID))')

        # create notify table
        # cur.execute('CREATE TABLE Notify( \
        #     ScheduleID INTEGER, \
        #     PersonID INTEGER, \
        #     FOREIGN KEY (ScheduleID) REFERENCES Schedule(ID) \
        #     FOREIGN KEY (PersonID) REFERENCES People(ID))')

        # commit changes
        con.commit()
        con.close()

        print('Good')

    except sqlite3.Error:
        # oh no
        print('oh no')

start()