'''

    Import create_engine from sqlalchemy.
    Create an engine to the census database by concatenating the following strings:
        'postgresql+psycopg2://'
        'student:datacamp'
        '@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com'
        ':5432/census'
    Use the .table_names() method on engine to print the table names.

'''
# Import create_engine function
from sqlalchemy import create_engine

# Create an engine to the census database
engine = create_engine('postgresql+psycopg2://student:datacamp@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com:5432/census')

# Use the .table_names() method on the engine to print the table names
print(engine.table_names())
