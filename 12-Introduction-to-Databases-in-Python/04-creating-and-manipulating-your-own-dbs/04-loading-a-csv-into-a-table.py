'''

    Create a statement for bulk insert into the census table. To do this, just use insert() and census.
    Create an empty list called values_list and a variable called total_rowcount that is set to 0.
    Within the for loop:
        Complete the data dictionary by filling in the values for each of the keys. The values are contained in row. row[0] represents the value for 'state', row[1] represents the value for 'sex', and so on.
        Append data to values_list.
        If 51 cleanly divides into the current idx:
            Execute stmt with the values_list and save it as results.
    Hit 'Submit Answer' to print total_rowcount when done with all the records.

'''
# Create a insert statement for census: stmt
stmt = insert(census)

# Create an empty list and zeroed row count: values_list, total_rowcount
values_list = []
total_rowcount = 0

# Enumerate the rows of csv_reader
for idx, row in enumerate(csv_reader):
    #create data and append to values_list
    data = {'state': row[0], 'sex': row[1], 'age': row[2], 'pop2000': row[3],
            'pop2008': row[4]}
    values_list.append(data)

    # Check to see if divisible by 51
    if idx % 51 == 0:
        results = connection.execute(stmt, values_list)
        total_rowcount += results.rowcount
        values_list = []

# Print total rowcount
print(total_rowcount)
