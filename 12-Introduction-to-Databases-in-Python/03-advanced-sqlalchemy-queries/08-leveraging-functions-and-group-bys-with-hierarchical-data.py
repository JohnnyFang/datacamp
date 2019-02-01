'''

    Save an alias of the employees table as managers.
    Build a query to select the name column of the managers table and the count of the number of their employees. The function func.count() has been imported and will be useful! Use it to count the id column of the employees table.
    Using a .where() clause, filter the records where the id column of the managers table and mgr column of the employees table are equal.
    Group the query by the name column of the managers table.
    Execute the statement and store all the results. Print the names of the managers and their employees. This code has already been written so hit 'Submit Answer' and check out the results!

'''
# Make an alias of the employees table: managers
managers = employees.alias()

# Build a query to select managers and counts of their employees: stmt
stmt = select([managers.columns.name, func.count(employees.columns.id)])

# Append a where clause that ensures the manager id and employee mgr are equal
stmt = stmt.where(managers.columns.id == employees.columns.mgr)

# Group by Managers Name
stmt = stmt.group_by(managers.columns.name)

# Execute statement: results
results = connection.execute(stmt).fetchall()

# print manager
for record in results:
    print(record)
