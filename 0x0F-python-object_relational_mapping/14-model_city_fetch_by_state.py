#!/usr/bin/python3
'''This is a module'''

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from model_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                           argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for i, j in session.query(State, City).filter(State.id == City.state_id):
        print(f"{i.name}: ({j.id}) {j.name}")
    session.close()
