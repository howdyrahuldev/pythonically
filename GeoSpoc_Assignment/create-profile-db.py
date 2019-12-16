import sqlite3

con = sqlite3.connect('my-profile-database.db')
cursorObj = con.cursor()
cursorObj.execute('CREATE TABLE profiles(eid text PRIMARY KEY, name text, site text, cover text, lovework text, file text)')
con.commit()
con.close()
