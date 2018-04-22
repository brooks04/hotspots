import sqlite3

def start():
    con = sqlite3.connect('schedule.db')
    cur = con.cursor()

    try:
        # create rooms table
        # cur.execute('CREATE TABLE Rooms(ID INTEGER PRIMARY KEY, Name TEXT NOT NULL)')
        # cur.execute('INSERT INTO Rooms VALUES(?, ?)', ('1', 'Room 1'))
        # cur.execute('INSERT INTO Rooms VALUES(?, ?)', ('2', 'Room 2'))
        # cur.execute('INSERT INTO Rooms VALUES(?, ?)', ('3', 'Room 3'))
        # cur.execute('INSERT INTO Rooms VALUES(?, ?)', ('4', 'Room 4'))

        # create people table
        # cur.execute('DROP TABLE People')
        # cur.execute('CREATE TABLE People(ID INTEGER PRIMARY KEY, PhoneNum INTEGER UNIQUE NOT NULL, SlackID TEXT UNIQUE NOT NULL, Name TEXT NOT NULL)')
        # cur.execute('INSERT INTO People VALUES(?, ?, ?, ?)', (1, 2532495291, 'UAAQRFKD1', 'Brooke Stevenson'))
        # cur.execute('INSERT INTO People VALUES(?, ?, ?, ?)', (2, 2064035739, 'UABQL3YQ6', 'Conor Marsten'))
        # cur.execute('INSERT INTO People VALUES(?, ?, ?, ?)', (3, 2537651034, 'UABV4R4DV', 'Alex Reid'))
        # cur.execute('INSERT INTO People VALUES(?, ?, ?, ?)', (4, 2145168410, 'UAA9E16E4', 'Tej Gidvani'))
        # cur.execute('INSERT INTO People VALUES(?, ?, ?, ?)', (5, 2538864895, 'UAA76JDCG', 'Alvin Nguyen'))

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

        # idList = []

        # person = 'Alex'
        # cur.execute('SELECT * FROM People WHERE Name LIKE ?', ('%' + person +'%',))
        # row = cur.fetchone()
        # idList.append(int(row[0]))
        
        # person = 'Brooke'
        # cur.execute('SELECT * FROM People WHERE Name LIKE ?', ('%' + person +'%',))
        # row = cur.fetchone()
        # idList.append(int(row[0]))
        
        # print(idList)

        cur.execute('ALTER TABLE Rooms ADD InUse INTEGER NOT NULL DEFAULT 0');

        con.commit()
        con.close()

        print('Good')

    except sqlite3.Error as e:
        # oh no
        print('oh no', e)

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

start()
readData()