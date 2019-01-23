'''

    Merge reshaped and hosts using an inner join. Remember, how='inner' is the default behavior for pd.merge().
    Print the first 5 rows of the DataFrame merged. This has been done for you. You should see that the rows are jumbled chronologically.
    Set the index of merged to be 'Edition' and sort the index.
    Print the first 5 rows of the DataFrame influence. This has been done for you, so hit 'Submit Answer' to see the results!

'''
# Import pandas
import pandas as pd

# Merge reshaped and hosts: merged
merged = pd.merge(reshaped, hosts)

# Print first 5 rows of merged
print(merged.head())

# Set Index of merged and sort it: influence
influence = merged.set_index('Edition').sort_index()

# Print first 5 rows of influence
print(influence.head())
