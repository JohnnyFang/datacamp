'''

    Modify the call to plt.contourf() so the filled contours in the top left subplot use the 'viridis' colormap.
    Modify the call to plt.contourf() so the filled contours in the top right subplot use the 'gray' colormap.
    Modify the call to plt.contourf() so the filled contours in the bottom left subplot use the 'autumn' colormap.
    Modify the call to plt.contourf() so the filled contours in the bottom right subplot use the 'winter' colormap.

'''
# Create a filled contour plot with a color map of 'viridis'
plt.subplot(2,2,1)
plt.contourf(X,Y,Z,20, cmap='viridis')
plt.colorbar()
plt.title('Viridis')

# Create a filled contour plot with a color map of 'gray'
plt.subplot(2,2,2)
plt.contourf(X,Y,Z,20, cmap='gray')
plt.colorbar()
plt.title('Gray')

# Create a filled contour plot with a color map of 'autumn'
plt.subplot(2,2,3)
plt.contourf(X,Y,Z,20, cmap='autumn')
plt.colorbar()
plt.title('Autumn')

# Create a filled contour plot with a color map of 'winter'
plt.subplot(2,2,4)
plt.contourf(X,Y,Z,20, cmap='winter')
plt.colorbar()
plt.title('Winter')

# Improve the spacing between subplots and display them
plt.tight_layout()
plt.show()
