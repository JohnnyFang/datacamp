'''

    Build a delete statement to remove data from the census table. Save it as stmt_del.
    Append a where clause to stmt_del that contains an and_ to filter for rows which have 'M' in the sex column AND 36 in the age column.
    Execute the delete statement.
    Hit 'Submit Answer' to print the rowcount of the results, as well as to_delete, which returns the number of rows that should be deleted. These should match and this is an important sanity check!

'''
# Build a statement to count records using the sex column for Men ('M') age 36: stmt
stmt = select([func.count(census.columns.sex)]).where(
    and_(census.columns.sex == 'M',
         census.columns.age == 36)
)

# Execute the select statement and use the scalar() fetch method to save the record count
to_delete = connection.execute(stmt).scalar()

# Build a statement to delete records from the census table: stmt_del
stmt_del = delete(census)

# Append a where clause to target Men ('M') age 36
stmt_del = stmt_del.where(
    and_(census.columns.sex == 'M',
         census.columns.age == 36)
)

# Execute the statement: results
results = connection.execute(stmt_del)

# Print affected rowcount and to_delete record count, make sure they match
print(results.rowcount, to_delete)
