#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object
    cur = db.cursor()

    # Execute SQL query
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows
    rows = cur.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()
