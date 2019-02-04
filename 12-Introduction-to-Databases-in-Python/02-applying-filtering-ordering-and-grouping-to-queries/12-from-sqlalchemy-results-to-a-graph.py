'''

    Import matplotlib.pyplot as plt.
    Create a DataFrame df using pd.DataFrame() on the provided results.
    Set the columns of the DataFrame df.columns to be the columns from the first result object results[0].keys().
    Print the DataFrame df.
    Use the plot.bar() method on df to create a bar plot of the results.
    Display the plot with plt.show().

'''
# Import pyplot as plt from matplotlib
import matplotlib.pyplot as plt

# Create a DataFrame from the results: df
df = pd.DataFrame(results)

# Set Column names
df.columns = results[0].keys()

# Print the DataFrame
print(df)

# Plot the DataFrame
df.plot.bar()
plt.show()