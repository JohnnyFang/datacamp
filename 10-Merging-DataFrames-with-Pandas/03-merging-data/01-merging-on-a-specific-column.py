'''

    Using pd.merge(), merge the DataFrames revenue and managers on the 'city' column of each. Store the result as merge_by_city.
    Print the DataFrame merge_by_city. This has been done for you.
    Merge the DataFrames revenue and managers on the 'branch_id' column of each. Store the result as merge_by_id.
    Print the DataFrame merge_by_id. This has been done for you, so hit 'Submit Answer' to see the result!

'''
# Merge revenue with managers on 'city': merge_by_city
merge_by_city = pd.merge(revenue, managers, on='city')

# Print merge_by_city
print(merge_by_city)

# Merge revenue with managers on 'branch_id': merge_by_id
merge_by_id = pd.merge(revenue, managers, on='branch_id')

# Print merge_by_id
print(merge_by_id)
