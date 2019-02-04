'''

    Build a statement to select all columns from the state_fact table where the name column is New York. Call it select_stmt.
    Print the results of executing the select_stmt and fetching all records.
    Build an update statement to change the fips_state column code to 36, save it as stmt.
    Use a where clause to filter for states with the name of 'New York' in the state_fact table.
    Execute stmt via the connection and save the output as results.
    Hit 'Submit Answer' to print the rowcount of the results and the results of executing select_stmt. This will verify the fips_state code is now 36.

'''
# Build a select statement: select_stmt
select_stmt = select([state_fact]).where(state_fact.columns.name == 'New York')

# Print the results of executing the select_stmt
print(connection.execute(select_stmt).fetchall())

# Build a statement to update the fips_state to 36: stmt
stmt = update(state_fact).values(fips_state = 36)

# Append a where clause to limit it to records for New York state
stmt = stmt.where(state_fact.columns.name == 'New York')

# Execute the statement: results
results = connection.execute(stmt)

# Print rowcount
print(results.rowcount)

# Execute the select_stmt again to view the changes
print(connection.execute(select_stmt).fetchall())
