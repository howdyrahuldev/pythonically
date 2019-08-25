"""
This project is for integradting Rest API with database, insert data through POST method and fetch data through GET method

First should run "create_table.py" for creating the database file and the table in it.
Then run "app.py" and call GET and POST methods as required.
"""

from flask import Flask, jsonify, request
import sqlite3
my_app = Flask(__name__)

@my_app.route('/adduser', methods=['POST'])
def insert_user():
    data=request.get_json()
    u=data['username']
    p=data['password']
    connection = sqlite3.connect('mydata.db')
    cursor = connection.cursor()
    insert_query = 'INSERT INTO users VALUES(?,?)'
    cursor.execute(insert_query, (u,p))
    connection.commit()
    connection.close()
    return jsonify({'message':'user added'})

@my_app.route('/displayusers')
def display():
    connection = sqlite3.connect('mydata.db')
    cursor = connection.cursor()

    display_query= 'SELECT * FROM users'
    results= cursor.execute(display_query)
    output=[]


    for row in results:
        output.append({"username":row[0],"password":row[1]})

    return jsonify({"users":output})

my_app.run(port=4078)