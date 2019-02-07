'''

    Compute the maximum enrollment of women in Computer Science using the .max() method.
    Calculate the year in which there was maximum enrollment of women in Computer Science using the .argmax() method.
    Annotate the plot with an arrow at the point of peak women enrolling in Computer Science.
        Label the arrow 'Maximum'. The parameter for this is s, but you don't have to specify it.
        Pass in the arguments to xy and xytext as tuples.
        For xy, use the yr_max and cs_max that you computed.
        For xytext, use (yr_max+5, cs_max+5) to specify the displacement of the label from the tip of the arrow.
        Draw the arrow by specifying the keyword argument arrowprops=dict(facecolor='black'). The single letter shortcut for 'black' is 'k'.

'''
# Plot with legend as before
plt.plot(year, computer_science, color='red', label='Computer Science')
plt.plot(year, physical_sciences, color='blue', label='Physical Sciences')
plt.legend(loc='lower right')

# Compute the maximum enrollment of women in Computer Science: cs_max
cs_max = computer_science.max()

# Calculate the year in which there was maximum enrollment of women in Computer Science: yr_max
yr_max = year[computer_science.argmax()]

# Add a black arrow annotation
plt.annotate('Maximum',xy=(yr_max, cs_max),
xytext=(yr_max+5, cs_max+5),
arrowprops=dict(facecolor='black'))

# Add axis labels and title
plt.xlabel('Year')
plt.ylabel('Enrollment (%)')
plt.title('Undergraduate enrollment of women')
plt.show()
