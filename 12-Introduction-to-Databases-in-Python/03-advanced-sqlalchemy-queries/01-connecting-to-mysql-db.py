'''

    Import the create_engine function from the sqlalchemy library.
    Create an engine to the census database by concatenating the following strings and passing them to create_engine():
        'mysql+pymysql://' (the dialect and driver).
        'student:datacamp' (the username and password).
        '@courses.csrrinzqubik.us-east-1.rds.amazonaws.com:3306/' (the host and port).
        'census' (the database name).
    Use the .table_names() method on engine to print the table names.

'''
# Import create_engine function
from sqlalchemy import create_engine

# Create an engine to the census database
engine = create_engine('mysql+pymysql://'+'student:datacamp'+'@courses.csrrinzqubik.us-east-1.rds.amazonaws.com:3306/'+'census')

# Print the table names
print(engine.table_names())
