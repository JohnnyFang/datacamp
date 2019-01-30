'''

    Import func from sqlalchemy.
    Build an expression to calculate the sum of the values in the pop2008 field labeled as 'population'.
    Build a select statement to get the value of the state field and the sum of the values in pop2008.
    Group the statement by state using a .group_by() method.
    Execute stmt using the connection to get the count and store the results as results.
    Print the keys/column names of the results returned using results[0].keys().

'''
# Import func
from sqlalchemy import func

# Build an expression to calculate the sum of pop2008 labeled as population
pop2008_sum = func.sum(census.columns.pop2008).label('population')

# Build a query to select the state and sum of pop2008: stmt
stmt = select([census.columns.state, pop2008_sum])

# Group stmt by state
stmt = stmt.group_by(census.columns.state)

# Execute the statement and store all the records: results
results = connection.execute(stmt).fetchall()

# Print results
print(results)

# Print the keys/column names of the results returned
print(results[0].keys())
