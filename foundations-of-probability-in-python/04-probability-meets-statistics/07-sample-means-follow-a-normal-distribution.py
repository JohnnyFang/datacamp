"""
Sample means follow a normal distribution

In the previous exercise, we generated a population that followed a binomial distribution, chose 20 random samples from the population, and calculated the sample mean. Now we're going to test some other probability distributions to see the shape of the sample means.

From the scipy.stats library, we've loaded the poisson and geom objects and the describe() function. We've also imported matplotlib.pyplot as plt and numpy as np.

As you'll see, the shape of the distribution of the means is the same even though the samples are generated from different distributions.
"""
#  1 Select 20 values from the population, add the sample mean to the sample_means list, and plot a histogram.
# Generate the population
population = geom.rvs(p=0.5, size=1000)

# Create list for sample means
sample_means = []
for _ in range(3000):
	# Take 20 values from the population
    sample = np.random.choice(population, 20)
    # Calculate the sample mean
    sample_means.append(describe(sample).mean)

# Plot the histogram
plt.hist(sample_means)
plt.show()


#  2 Select 20 values from the population, populate the sample_means list, and plot a histogram.
# Generate the population
population = poisson.rvs(mu=2, size=1000)

# Create list for sample means
sample_means = []
for _ in range(1500):
	# Take 20 values from the population
    sample = np.random.choice(population, 20)
    # Calculate the sample mean
    sample_means.append(describe(sample).mean)

# Plot the histogram
plt.hist(sample_means)
plt.show()
