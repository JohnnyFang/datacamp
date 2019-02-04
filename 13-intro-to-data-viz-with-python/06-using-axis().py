'''

    Use plt.axis() to select the time period between 1990 and 2010 on the x-axis as well as the interval between 0 and 50% awarded on the y-axis.
    Save the resulting plot as 'axis_limits.png'.

'''
# Plot in blue the % of degrees awarded to women in Computer Science
plt.plot(year,computer_science, color='blue')

# Plot in red the % of degrees awarded to women in the Physical Sciences
plt.plot(year, physical_sciences,color='red')

# Set the x-axis and y-axis limits
plt.axis((1990,2010,0,50))

# Show the figure
plt.show()

# Save the figure as 'axis_limits.png'
plt.savefig('axis_limits.png')
