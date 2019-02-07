'''

    Generate a two-dimensional histogram with plt.hexbin() to view the joint variation of the mpg and hp vectors.
    Put hp along the horizontal axis and mpg along the vertical axis.
    Specify a hexagonal tesselation with 15 hexagons across the x-direction and 12 hexagons across the y-direction using gridsize.
    Specify the rectangular region covered with the optional extent argument: use hp from 40 to 235 and mpg from 8 to 48.
    Add a color bar to the histogram.

'''
# Generate a 2d histogram with hexagonal bins
plt.hexbin(hp, mpg, gridsize=(15, 12), extent = (40,235,8,48))


# Add a color bar to the histogram
plt.colorbar()

# Add labels, title, and display the plot
plt.xlabel('Horse power [hp]')
plt.ylabel('Miles per gallon [mpg]')
plt.title('hexbin() plot')
plt.show()
