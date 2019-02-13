'''

    Import matplotlib.pyplot and seaborn using the standard names plt and sns respectively.
    Generate a green residual plot of the regression between 'hp' (on the x-axis) and 'mpg' (on the y-axis). You will need to specify the additional data and color parameters.
    Display the plot as usual using plt.show(). This has been done for you, so hit 'Submit Answer' to view the plot.

'''
# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns

# Generate a green residual plot of the regression between 'hp' and 'mpg'
sns.residplot(x='hp', y='mpg', data=auto, color='green')

# Display the plot
plt.show()
