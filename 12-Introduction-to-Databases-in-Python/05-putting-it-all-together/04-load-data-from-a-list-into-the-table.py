'''

    Import insert from sqlalchemy.
    Build an insert statement for the census table.
    Execute the statement stmt along with values_list. You will need to pass them both as arguments to connection.execute().
    Print the rowcount attribute of results.

'''
# Import insert
from sqlalchemy import insert

# Build insert statement: stmt
stmt = insert(census)

# Use values_list to insert data: results
results = connection.execute(stmt, values_list)

# Print rowcount
print(results.rowcount)
