'''

    Generate a two-dimensional histogram to view the joint variation of the mpg and hp arrays.
    Put hp along the horizontal axis and mpg along the vertical axis.
    Specify 20 by 20 rectangular bins with the bins argument.
    Specify the region covered with the optional range argument so that the plot samples hp between 40 and 235 on the x-axis and mpg between 8 and 48 on the y-axis.
    Add a color bar to the histogram.

'''
# Generate a 2-D histogram
plt.hist2d(hp, mpg, bins=(20, 20), range=[[40, 235], [8, 48]])

# Add a color bar to the histogram
plt.colorbar()

# Add labels, title, and display the plot
plt.xlabel('Horse power [hp]')
plt.ylabel('Miles per gallon [mpg]')
plt.title('hist2d() plot')
plt.show()
