'''

    Import matplotlib.pyplot and seaborn using the standard names plt and sns respectively.
    Plot a linear regression between the 'weight' column (on the x-axis) and the 'hp' column (on the y-axis) from the DataFrame auto.
    Display the plot as usual with plt.show(). This has been done for you, so hit 'Submit Answer' to view the plot.

'''
# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns

# Plot a linear regression between 'weight' and 'hp'
sns.lmplot(x='weight', y='hp', data=auto)

# Display the plot
plt.show()
