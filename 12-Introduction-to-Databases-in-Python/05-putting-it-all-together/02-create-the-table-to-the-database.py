'''

    Import Table, Column, String, and Integer from sqlalchemy.
    Define a census table with the following columns:
        'state' - String - length of 30
        'sex' - String - length of 1
        'age' - Integer
        'pop2000' - Integer
        'pop2008' - Integer
    Create the table in the database using the metadata and engine.

'''
# Import Table, Column, String, and Integer
from sqlalchemy import Table, Column, String, Integer

# Build a census table: census
census = Table('census', metadata,
               Column('state', String(30)),
               Column('sex', String(1)),
               Column('age', Integer()),
               Column('pop2000', Integer()),
               Column('pop2008', Integer()))

# Create the table in the database
metadata.create_all(engine)
