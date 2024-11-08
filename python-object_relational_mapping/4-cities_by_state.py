#!/usr/bin/python3

"""
import code
"""

import MySQLdb
import sys

"""
code
"""

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )

    cursor = db.cursor()

    cursor.execute("SELECT cities.id, cities.name, states.name "
                   "FROM cities JOIN states "
                   "ON cities.state_id = states.id "
                   "ORDER BY cities.id ASC;")

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    db.close()
