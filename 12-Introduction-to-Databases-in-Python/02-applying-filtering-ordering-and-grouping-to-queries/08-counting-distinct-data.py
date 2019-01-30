'''

    Build a select statement to count the distinct values in the state field of census.
    Execute stmt to get the count and store the results as distinct_state_count.
    Print the value of distinct_state_count.

'''
# Build a query to count the distinct states values: stmt
stmt = select([func.count(census.columns.state.distinct())])

# Execute the query and store the scalar result: distinct_state_count
distinct_state_count = connection.execute(stmt).scalar()

# Print the distinct_state_count
print(distinct_state_count)
