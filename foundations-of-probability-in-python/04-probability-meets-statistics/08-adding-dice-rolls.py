"""
Adding dice rolls

To illustrate the central limit theorem, we are going to work with dice rolls. We'll generate the samples and then add them to plot the outcome.

You're provided with a function named roll_dice() that will generate the sample dice rolls. numpy is already imported as np for your convenience: you have to use np.add(sample1, sample2) to add samples. Also, matplotlib.pyplot is imported as plt so you can plot the histograms.
"""

#  1 Generate a sample of dice rolls using roll_dice(2000) and plot a histogram of the sample.
# Configure random generator
np.random.seed(42)

# Generate the sample
sample1 = roll_dice(2000)

# Plot the sample
plt.hist(sample1, bins=range(1, 8), width=0.9)
plt.show()


#  2 Add sample1 and sample2 using np.add(), store the result in the variable sum_of_1_and_2, then plot sum_of_1_and_2.
# Configure random generator
np.random.seed(42)

# Generate the samples
sample1 = roll_dice(2000)
sample2 = roll_dice(2000)

# Add the first two samples
sum_of_1_and_2 = np.add(sample1, sample2)

# Plot the sum
plt.hist(sum_of_1_and_2, bins=range(2, 14), width=0.9)
plt.show()


#  3 Add sum_of_1_and_2 and sample3 using np.add() and store the result in sum_of_3_samples. Then plot sum_of_3_samples.

# Configure random generator
np.random.seed(42)

# Generate the samples
sample1 = roll_dice(2000)
sample2 = roll_dice(2000)
sample3 = roll_dice(2000)

# Add the first two samples
sum_of_1_and_2 = np.add(sample1, sample2)

# Add the first two with the third sample
sum_of_3_samples = np.add(sum_of_1_and_2, sample3)

# Plot the result
plt.hist(sum_of_3_samples, bins=range(3, 20), width=0.9)
plt.show()
