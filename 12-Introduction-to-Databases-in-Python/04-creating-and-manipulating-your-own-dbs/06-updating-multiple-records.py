'''

    Build an update statement to update the notes column in the state_fact table to 'The Wild West'. Save it as stmt.
    Use a where clause to filter for records that have 'West' in the census_region_name column of the state_fact table.
    Execute stmt via the connection and save the output as results.
    Hit 'Submit Answer' to print rowcount of the results.

'''
# Build a statement to update the notes to 'The Wild West': stmt
stmt = update(state_fact).values(notes='The Wild West')

# Append a where clause to match the West census region records
stmt = stmt.where(state_fact.columns.census_region_name == 'West')

# Execute the statement: results
results = connection.execute(stmt)

# Print rowcount
print(results.rowcount)
