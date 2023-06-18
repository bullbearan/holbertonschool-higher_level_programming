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
    sql_query = """SELECT cities.id, cities.name, states.name FROM states,
                cities WHERE states.id = state_id"""
    cursor.execute(sql_query)
    for i in cursor:
        print(i)
    cursor.close()
    db.close()
