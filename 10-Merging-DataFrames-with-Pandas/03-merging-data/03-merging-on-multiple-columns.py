'''

    Create a column called 'state' in the DataFrame revenue, consisting of the list ['TX','CO','IL','CA'].
    Create a column called 'state' in the DataFrame managers, consisting of the list ['TX','CO','CA','MO'].
    Merge the DataFrames revenue and managers using three columns :'branch_id', 'city', and 'state'. Pass them in as a list to the on paramater of pd.merge().

'''
# Add 'state' column to revenue: revenue['state']
revenue['state'] = ['TX','CO','IL','CA']

# Add 'state' column to managers: managers['state']
managers['state'] = ['TX','CO','CA','MO']

# Merge revenue & managers on 'branch_id', 'city', & 'state': combined
combined = pd.merge(revenue, managers, on=['branch_id', 'city', 'state'])

# Print combined
print(combined)
