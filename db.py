import sqlite3

conn = sqlite3.connect('mydb.db')
print("Opened database successfully")

conn.execute('CREATE TABLE user (first_name TEXT, email TEXT, password TEXT)')
print("Table created successfully")
conn.close()
