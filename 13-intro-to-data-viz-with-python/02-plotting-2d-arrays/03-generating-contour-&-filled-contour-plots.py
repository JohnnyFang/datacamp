'''

    Using the meshgrid X, Y as axes:
        Generate a default contour plot of the array Z in the upper left subplot.
        Generate a contour plot of the array Z in the upper right subplot with 20 contours.
        Generate a default filled contour plot of the array Z in the lower left subplot.
        Generate a default filled contour plot of the array Z in the lower right subplot with 20 contours.
    Improve the spacing between the subplots with plt.tight_layout() and display the figure.

'''
# Generate a default contour map of the array Z
plt.subplot(2,2,1)
plt.contour(Z)

# Generate a contour map with 20 contours
plt.subplot(2,2,2)
plt.contour(Z, 20)

# Generate a default filled contour map of the array Z
plt.subplot(2,2,3)
plt.contourf(Z)

# Generate a default filled contour map with 20 contours
plt.subplot(2,2,4)
plt.contourf(Z, 20)

# Improve the spacing between subplots
plt.tight_layout()

# Display the figure
plt.show()
