'''

    Import func from sqlalchemy.
    Build a select statement to get the value of the state field and a count of the values in the age field, and store it as stmt.
    Use the .group_by() method to group the statement by the state column.
    Execute stmt using the connection to get the count and store the results as results.
    Print the keys/column names of the results returned using results[0].keys().

'''
# Import func
from sqlalchemy import func

# Build a query to select the state and count of ages by state: stmt
stmt = select([census.columns.state, func.count(census.columns.age)])

# Group stmt by state
stmt = stmt.group_by(census.columns.state)

# Execute the statement and store all the records: results
results = connection.execute(stmt).fetchall()

# Print results
print(results)

# Print the keys/column names of the results returned
print(results[0].keys())
