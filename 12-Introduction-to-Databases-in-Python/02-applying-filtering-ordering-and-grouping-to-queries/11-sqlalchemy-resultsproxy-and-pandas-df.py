'''

    Import pandas as pd.
    Create a DataFrame df using pd.DataFrame() on the ResultProxy results.
    Set the columns of the DataFrame df.columns to be the columns from the first result object results[0].keys().
    Print the DataFrame.

'''
# import pandas
import pandas as pd

# Create a DataFrame from the results: df
df = pd.DataFrame(results)

# Set column names
df.columns = results[0].keys()

# Print the Dataframe
print(df)
