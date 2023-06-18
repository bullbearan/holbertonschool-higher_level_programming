#!/usr/bin/python3
'''This is a module'''

import MySQLdb
from sys import argv
mysql = MySQLdb


if __name__ == "__main__":
    db = mysql.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                   .format(argv[4]))
    for i in cursor:
        print(i)
    cursor.close()
    db.close()
