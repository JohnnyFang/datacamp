'''

    Modify the plot command provided that draws the enrollment of women in Computer Science over time so that the curve is labelled 'Computer Science' in the legend.
    Modify the plot command provided that draws the enrollment of women in the Physical Sciences over time so that the curve is labelled 'Physical Sciences' in the legend.
    Add a legend at the lower center (i.e., loc='lower center').

'''
# Specify the label 'Computer Science'
plt.plot(year, computer_science, color='red', label='Computer Science')

# Specify the label 'Physical Sciences'
plt.plot(year, physical_sciences, color='blue', label='Physical Sciences')

# Add a legend at the lower center
plt.legend(loc='lower center')

# Add axis labels and title
plt.xlabel('Year')
plt.ylabel('Enrollment (%)')
plt.title('Undergraduate enrollment of women')
plt.show()
