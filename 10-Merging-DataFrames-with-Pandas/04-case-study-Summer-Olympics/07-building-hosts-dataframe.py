'''

    Create the DataFrame hosts by doing a left join on DataFrames editions and ioc_codes (using pd.merge()).
    Clean up hosts by subsetting and setting the Index.
        Extract the columns 'Edition' and 'NOC'.
        Set 'Edition' column as the Index.
    Use the .loc[] accessor to find and assign the missing values to the 'NOC' column in hosts. This has been done for you.
    Reset the index of hosts using .reset_index(), which you'll need to save as the hosts DataFrame.
    Hit 'Submit Answer' to see what hosts looks like!

'''
# Import pandas
import pandas as pd

# Left join editions and ioc_codes: hosts
hosts = pd.merge(editions, right=ioc_codes, how='left')

# Extract relevant columns and set index: hosts
hosts = hosts[['Edition', 'NOC']].set_index('Edition')

# Fix missing 'NOC' values of hosts
print(hosts.loc[hosts.NOC.isnull()])
hosts.loc[1972, 'NOC'] = 'FRG'
hosts.loc[1980, 'NOC'] = 'URS'
hosts.loc[1988, 'NOC'] = 'KOR'

# Reset Index of hosts: hosts
hosts = hosts.reset_index()

# Print hosts
print(hosts)
