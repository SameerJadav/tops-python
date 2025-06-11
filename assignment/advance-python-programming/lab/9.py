# Write a Python program to connect to an SQLite3 database, create a table, insert data, and fetch data

import sqlite3

# connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER
    )
""")

# insert data
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("sameer", 21))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("bhoomi", 21))
conn.commit()

# fetch data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)

# close the connection
conn.close()
