#!/usr/bin/python3
import sqlite3

def print_form_info(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    # cursor.execute("select name from sqlite_master where type == 'table'")
    result = cursor.execute("select * from moz_cookies")
    for row in result:
        print("{}\n".format(row))

if __name__ == "__main__":
    print_form_info("/home/hacker/Desktop/sqlite/cookies.sqlite")