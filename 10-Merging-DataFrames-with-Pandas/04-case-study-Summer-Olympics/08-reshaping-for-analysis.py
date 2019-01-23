'''

    Create a DataFrame reshaped by reshaping the DataFrame fractions_change with pd.melt().
    You'll need to use the keyword argument id_vars='Edition' to set the identifier variable.
    You'll also need to use the keyword argument value_name='Change' to set the measured variables.
    Print the shape of the DataFrames reshaped and fractions_change. This has been done for you.
    Create a DataFrame chn by extracting all the rows from reshaped in which the three letter code for each country ('NOC') is 'CHN'.
    Print the last 5 rows of the DataFrame chn using the .tail() method. This has been done for you, so hit 'Submit Answer' to see the results!

'''
# Import pandas
import pandas as pd

# Reshape fractions_change: reshaped
reshaped = pd.melt(fractions_change, id_vars='Edition', value_name='Change')

# Print reshaped.shape and fractions_change.shape
print(reshaped.shape, fractions_change.shape)

# Extract rows from reshaped where 'NOC' == 'CHN': chn
chn = reshaped[reshaped['NOC'] == 'CHN']

# Print last 5 rows of chn with .tail()
print(chn.tail())
