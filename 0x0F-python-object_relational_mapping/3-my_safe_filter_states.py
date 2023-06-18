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
    sql_query = "SELECT * FROM states WHERE name = %s"
    cursor.execute(sql_query, (argv[4], ))
    for i in cursor:
        print(i)
    cursor.close()
    db.close()
