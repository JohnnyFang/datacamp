'''

    Merge the DataFrames revenue and managers into a single DataFrame called combined using the 'city' and 'branch' columns from the appropriate DataFrames.
        In your call to pd.merge(), you will have to specify the parameters left_on and right_on appropriately.
    Print the new DataFrame combined.

'''
# Merge revenue & managers on 'city' & 'branch': combined
combined = pd.merge(revenue, managers, left_on='city', right_on='branch')

# Print combined
print(combined)
