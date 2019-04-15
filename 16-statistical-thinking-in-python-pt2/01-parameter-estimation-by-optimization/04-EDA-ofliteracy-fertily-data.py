'''
EDA of literacy/fertility data
In the next few exercises, we will look at the correlation between female literacy and fertility (defined as the average number of children born per woman) throughout the world. For ease of analysis and interpretation, we will work with the illiteracy rate.

It is always a good idea to do some EDA ahead of our analysis. To this end, plot the fertility versus illiteracy and compute the Pearson correlation coefficient. The Numpy array illiteracy has the illiteracy rate among females for most of the world's nations. The array fertility has the corresponding fertility data.

Here, it may be useful to refer back to the function you wrote in the previous course to compute the Pearson correlation coefficient.

Instructions
    Plot fertility (y-axis) versus illiteracy (x-axis) as a scatter plot.
    Set a 2% margin.
    Compute and print the Pearson correlation coefficient between illiteracy and fertility.

'''
# Plot the illiteracy rate versus fertility
_ = plt.plot(illiteracy, fertility, marker='.', linestyle='none')

# Set the margins and label axes
plt.margins(0.02)
_ = plt.xlabel('percent illiterate')
_ = plt.ylabel('fertility')

# Show the plot
plt.show()

# Show the Pearson correlation coefficient
print(pearson_r(illiteracy, fertility))

#  You can see the correlation between illiteracy and fertility by eye, and by
# the substantial Pearson correlation coefficient of 0.8. It is difficult to
# resolve in the scatter plot, but there are many points around near-zero
#  illiteracy and about 1.8 children/woman.
