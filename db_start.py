import sqlite3

con = sqlite3.connect('user_info.db')
cur = con.cursor()

# try:
#     cur.execute('CREATE TABLE user_info(username TEXT NOT NULL, password TEXT NOT NULL)')
#     print('Table made')

# except sqlite3.Error:
#     print('oops')

# cur.execute('INSERT INTO user_info VALUES (?, ?)', ('user@hello.com', 'password'))
# con.commit()
cur.execute('SELECT * FROM user_info')
print(cur.fetchall())