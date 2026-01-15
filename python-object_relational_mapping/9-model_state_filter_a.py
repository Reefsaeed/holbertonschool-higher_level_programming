#!/usr/bin/python3
"""
Lists all State objects that contain the letter a
from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine to connect to MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database), pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query State objects that contain 'a' in name, ordered by id
    # Use ilike for case-insensitive match (contains 'a' or 'A')
    states = session.query(State).filter(
        State.name.like('%a%')
    ).order_by(State.id).all()

    # Print each state in the required format
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
