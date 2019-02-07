'''

    Use plt.xlim() to set the x-axis range to the period between the years 1990 and 2010.
    Use plt.ylim() to set the y-axis range to the interval between 0% and 50% of degrees awarded.
    Display the final figure with plt.show() and save the output to 'xlim_and_ylim.png'.

'''
# Plot the % of degrees awarded to women in Computer Science and the Physical Sciences
plt.plot(year,computer_science, color='red')
plt.plot(year, physical_sciences, color='blue')

# Add the axis labels
plt.xlabel('Year')
plt.ylabel('Degrees awarded to women (%)')

# Set the x-axis range
plt.xlim((1990,2010))

# Set the y-axis range
plt.ylim((0, 50))

# Add a title and display the plot
plt.title('Degrees awarded to women (1990-2010)\nComputer Science (red)\nPhysical Sciences (blue)')
plt.show()

# Save the image as 'xlim_and_ylim.png'
plt.savefig('xlim_and_ylim.png')
