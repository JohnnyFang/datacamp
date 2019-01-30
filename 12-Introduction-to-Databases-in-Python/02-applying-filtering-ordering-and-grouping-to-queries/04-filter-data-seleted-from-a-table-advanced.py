'''

    Import and_ from the sqlalchemy module.
    Select all records from the census table.
    Append a where clause to filter all the records whose state is 'California', and whose sex is not 'M'.
    Iterate over the ResultProxy and print the age and sex columns from each record.

'''
# Import and_
from sqlalchemy import and_

# Build a query for the census table: stmt
stmt = select([census])

# Append a where clause to select only non-male records from California using and_
stmt = stmt.where(
    # The state of California with a non-male sex
    and_(census.columns.state == 'California',
         census.columns.sex != 'M'
         )
)

# Loop over the ResultProxy printing the age and sex
for result in connection.execute(stmt).fetchall():
    print(result.age, result.sex)
