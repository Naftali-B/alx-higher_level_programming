#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=mysql_user,
                         passwd=mysql_password,
                         db=database_name)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()

