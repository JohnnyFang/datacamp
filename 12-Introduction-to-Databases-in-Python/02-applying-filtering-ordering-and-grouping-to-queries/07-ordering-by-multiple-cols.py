'''

    Select all records of the state and age columns from the census table.
    Use .order_by() to sort the output of the state column in ascending order and age in descending order. (NOTE: desc is already imported).
    Execute stmt using the .execute() method on connection and retrieve all the results using .fetchall().
    Print the first 20 results.

'''
# Build a query to select state and age: stmt
stmt = select([census.columns.state, census.columns.age])

# Append order by to ascend by state and descend by age
stmt = stmt.order_by(census.columns.state, desc(census.columns.age))

# Execute the statement and store all the records: results
results = connection.execute(stmt).fetchall()

# Print the first 20 results
print(results[:20])
