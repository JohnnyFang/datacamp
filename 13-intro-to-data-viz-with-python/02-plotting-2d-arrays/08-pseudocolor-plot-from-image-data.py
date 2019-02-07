'''

    Print the shape of the existing image array.
    Compute the sum of the red, green, and blue channels of img by using the .sum() method with axis=2.
    Print the shape of the intensity array to verify this is the shape you expect.
    Plot intensity with plt.imshow() using a 'gray' colormap.
    Add a colorbar to the figure.

'''
# Load the image into an array: img
img = plt.imread('480px-Astronaut-EVA.jpg')

# Print the shape of the image
print(img.shape)

# Compute the sum of the red, green and blue channels: intensity
intensity = img.sum(axis=2)

# Print the shape of the intensity
print(intensity.shape)

# Display the intensity with a colormap of 'gray'
plt.imshow(intensity, cmap='gray')

# Add a colorbar
plt.colorbar()

# Hide the axes and show the figure
plt.axis('off')
plt.show()
