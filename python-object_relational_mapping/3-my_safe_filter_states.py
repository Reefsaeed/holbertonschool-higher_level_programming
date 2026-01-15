#!/usr/bin/python3
"""
Takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
Safe from MySQL injections.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

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

    # Create SQL query with parameterized input (safe from SQL injection)
    # Use %s as placeholder, MySQLdb will sanitize the input
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    # Execute SQL query with state_name as parameter (tuple)
    cur.execute(query, (state_name,))

    # Fetch all rows
    rows = cur.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()
