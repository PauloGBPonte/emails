import sqlite3

conn = sqlite3.connect('emails.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS emails (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT)''')


conn.commit()
conn.close()
