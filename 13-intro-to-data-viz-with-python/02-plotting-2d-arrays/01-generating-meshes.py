'''

    Import the numpy and matplotlib.pyplot modules using the respective aliases np and plt.
    Generate two one-dimensional arrays u and v using np.linspace(). The array u should contain 41 values uniformly spaced beween -2 and +2. The array v should contain 21 values uniformly spaced between -1 and +1.
    Construct two two-dimensional arrays X and Y from u and v using np.meshgrid(). The resulting arrays should have shape (41,21).
    After the array Z is computed using X and Y, visualize the array Z using plt.pcolor() and plt.show().
    Save the resulting figure as 'sine_mesh.png'.

'''
# Import numpy and matplotlib.pyplot
import matplotlib.pyplot as plt
import numpy as np

# Generate two 1-D arrays: u, v
u = np.linspace(-2, 2, num=41)
v = np.linspace(-1, 1, num=21)

# Generate 2-D arrays from u and v: X, Y
X,Y = np.meshgrid(u, v)

# Compute Z based on X and Y
Z = np.sin(3*np.sqrt(X**2 + Y**2))

# Display the resulting image with pcolor()
plt.pcolor(Z)
plt.show()

# Save the figure to 'sine_mesh.png'
plt.savefig('sine_mesh.png')
