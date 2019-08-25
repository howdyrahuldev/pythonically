import sqlite3

connection = sqlite3.connect('mydata.db')
cursor = connection.cursor()




create_query = 'CREATE TABLE IF NOT EXISTS users(username text, password text)'

cursor.execute(create_query)
connection.commit()
connection.close()



