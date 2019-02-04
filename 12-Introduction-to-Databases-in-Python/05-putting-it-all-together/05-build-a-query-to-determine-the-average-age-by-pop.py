'''

    Import select from sqlalchemy.
    Build a statement to:
        Select sex from the census table.
        Select the average age weighted by the population in 2008 (pop2008). See the example given in the assignment text to see how you can do this. Label this average age calculation as 'average_age'.
    Group the query by sex.
    Execute the query and store it as results.
    Loop over results and print the sex and average_age for each record.

'''
# Import select
from sqlalchemy import select

# Calculate weighted average age: stmt
stmt = select([census.columns.sex,
               (func.sum(census.columns.pop2008 * census.columns.age) /
                func.sum(census.columns.pop2008)).label('average_age')
               ])

# Group by sex
stmt = stmt.group_by(census.columns.sex)

# Execute the query and store the results: results
results = connection.execute(stmt).fetchall()

# Print the average age by sex
for result in results:
    print(result[0], result[1])
