'''

    Use plt.subplot() to create a figure with 1x2 subplot layout & make the first subplot active.
    Plot the percentage of degrees awarded to women in Physical Sciences in blue in the active subplot.
    Use plt.subplot() again to make the second subplot active in the current 1x2 subplot grid.
    Plot the percentage of degrees awarded to women in Computer Science in red in the active subplot.

'''
# Create a figure with 1x2 subplot and make the left subplot active
plt.subplot(1, 2, 1)

# Plot in blue the % of degrees awarded to women in the Physical Sciences
plt.plot(year, physical_sciences, color='blue')
plt.title('Physical Sciences')

# Make the right subplot active in the current 1x2 subplot grid
plt.subplot(1, 2, 2)

# Plot in red the % of degrees awarded to women in Computer Science
plt.plot(year, computer_science, color='red')
plt.title('Computer Science')

# Use plt.tight_layout() to improve the spacing between subplots
plt.tight_layout()
plt.show()
