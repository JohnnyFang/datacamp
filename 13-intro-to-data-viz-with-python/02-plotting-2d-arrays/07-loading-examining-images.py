'''

    Load the file '480px-Astronaut-EVA.jpg' into an array.
    Print the shape of the img array. How wide and tall do you expect the image to be?
    Prepare img for display using plt.imshow().
    Turn off the axes using plt.axis('off').

'''
# Load the image into an array: img
img = plt.imread('480px-Astronaut-EVA.jpg')

# Print the shape of the image
print(img.shape)

# Display the image
plt.imshow(img)

# Hide the axes
plt.axis('off')
plt.show()
