"""
Sample means

An important result in probability and statistics is that the shape of the distribution of the means of random variables tends to a normal distribution, which happens when you add random variables with any distribution with the same expected value and variance.

For your convenience, we've loaded binom and describe() from the scipy.stats library and imported matplotlib.pyplot as plt and numpy as np. We generated a simulated population with size 1,000 that follows a binomial distribution for 10 fair coin flips and is available in the population variable.
"""
# Create list for sample means
sample_means = []
for _ in range(1500):
	# Take 20 values from the population
    sample = np.random.choice(population, 20)
    # Calculate the sample mean
    sample_means.append(describe(sample).mean)

# Plot the histogram
plt.hist(sample_means)
plt.xlabel("Sample mean values")
plt.ylabel("Frequency")
plt.show()
