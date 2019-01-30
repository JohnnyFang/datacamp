'''

    Select all records from the census table by passing it in as a list to select().
    Append a where clause to return all the records with a state in the states list. Use in_(states) on census.columns.state to do this.
    Loop over the ResultProxy connection.execute(stmt) and print the state and pop2000 columns from each record.

'''
# Create a query for the census table: stmt
stmt = select([census])

# Append a where clause to match all the states in_ the list states
stmt = stmt.where(census.columns.state.in_(states))

# Loop over the ResultProxy and print the state and its population in 2000
for result in connection.execute(stmt):
    print(result.state, result.pop2000)
