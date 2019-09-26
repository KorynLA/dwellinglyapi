import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

# MUST BE INTEGER
# This is the only place where int vs INTEGER matters—in auto-incrementing columns
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS properties (id INTEGER PRIMARY KEY, name text, address text, zipCode INTEGER, city text, state text)"
cursor.execute(create_table)
cursor.execute("INSERT INTO properties VALUES ( 1,'Garden Blocks', '1654 NE 18th Ave.', 97218, 'Portland', 'OR')")

connection.commit()

connection.close()
