'''
You will now use your ecdf() function to compute the ECDF for the petal lengths of Anderson's Iris versicolor flowers. You will then plot the ECDF. Recall that your ecdf() function returns two arrays so you will need to unpack them. An example of such unpacking is x, y = foo(data), for some function foo().

Instructions
    Use ecdf() to compute the ECDF of versicolor_petal_length. Unpack the output into x_vers and y_vers.
    Plot the ECDF as dots. Remember to include marker = '.' and linestyle = 'none' in addition to x_vers and y_vers as arguments inside plt.plot().
    Label the axes. You can label the y-axis 'ECDF'.
    Show your plot.
'''
# Compute ECDF for versicolor data: x_vers, y_vers
x_vers, y_vers  = ecdf(versicolor_petal_length)

# Generate plot
plt.plot(x_vers, y_vers, marker = '.', linestyle = 'none')

# Label the axes
plt.xlabel('petal length (cm)')
plt.ylabel('ECDF')

# Display the plot
plt.show()
