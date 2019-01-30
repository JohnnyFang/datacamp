'''

    Select all records from the census table by passing in census as a list to select().
    Append a where clause to stmt to return only the records with a state of 'New York'.
    Execute the statement stmt using .execute() and retrieve the results using .fetchall().
    Iterate over results and print the age, sex and pop2008 columns from each record. For example, you can print out the age of result with result.age.

'''
# Create a select query: stmt
stmt = select([census])

# Add a where clause to filter the results to only those for New York
stmt = stmt.where(census.columns.state == 'New York')

# Execute the query to retrieve all the data returned: results
results = connection.execute(stmt).fetchall()

# Loop over the results and print the age, sex, and pop2008
for result in results:
    print(result.age, result.sex, result.pop2008)
