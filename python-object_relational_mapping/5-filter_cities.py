#!/usr/bin/python3
"""
Takes in the name of a state as an argument and lists all cities of that state
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

    # Execute SQL query - parameterized to prevent SQL injection
    # Get cities for the specified state
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """

    cur.execute(query, (state_name,))

    # Fetch all rows
    rows = cur.fetchall()

    # Extract city names from rows and join with comma and space
    city_names = [row[0] for row in rows]
    print(", ".join(city_names))

    # Close cursor and database connection
    cur.close()
    db.close()
