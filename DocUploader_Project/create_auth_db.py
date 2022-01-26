import sqlite3

con = sqlite3.connect('my-auth-database.db')
cursorObj = con.cursor()
cursorObj.execute('CREATE TABLE userauth(eid text PRIMARY KEY, password text)')
con.commit()
con.close()
