'''

    Build a statement to join the census and state_fact tables and select the pop2000 column from the first and the abbreviation column from the second.
    Execute the statement to get the first result and save it as result.
    Hit 'Submit Answer' to loop over the keys of the result object, and print the key and value for each!

'''
# Build a statement to join census and state_fact tables: stmt
stmt = select([census.columns.pop2000, state_fact.columns.abbreviation])

# Execute the statement and get the first result: result
result = connection.execute(stmt).first()

# Loop over the keys in the result object and print the key and value
for key in result.keys():
    print(key, getattr(result, key))
