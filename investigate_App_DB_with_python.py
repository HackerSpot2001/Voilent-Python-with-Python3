#!/usr/bin/python3
import sqlite3

conn = sqlite3.connect("/home/hacker/Desktop/Databases.db")
cursor = conn.cursor()

# Fetch All Tables From Database
# fetch_all = cursor.execute("SELECT name FROM sqlite_master WHERE type == 'table'")
# print(fetch_all.fetchall())

# Get Columns From tabel
# names = list(map(lambda X:X[0], cursor.description))

# Get All Data From COMPANY
for result in cursor.execute("SELECT * FROM COMPANY"):
    print(result)