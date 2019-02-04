'''
You will issue two plt.plot() commands to draw line plots of different colors on the same set of axes. Here, year represents the x-axis, while physical_sciences and computer_science are the y-axes.

    Import matplotlib.pyplot as its usual alias.
    Add a 'blue' line plot of the % of degrees awarded to women in the Physical Sciences (physical_sciences) from 1970 to 2011 (year). Note that the x-axis should be specified first.
    Add a 'red' line plot of the % of degrees awarded to women in Computer Science (computer_science) from 1970 to 2011 (year).
    Use plt.show() to display the figure with the curves on the same axes.

'''
# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Plot in blue the % of degrees awarded to women in the Physical Sciences
plt.plot(year, physical_sciences, color='blue')

# Plot in red the % of degrees awarded to women in Computer Science
plt.plot(year, computer_science, color='red')

# Display the plot
plt.show()
