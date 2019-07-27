"""
Calculating the sample mean

Simulation involves generating samples and then measuring. In this exercise, we'll generate some samples and calculate the sample mean with the describe() method. See what you observe about the sample mean as the number of samples increases.

We've preloaded the binom object and the describe() method from scipy.stats for you, so you can calculate some values.

Instructions 1/3
    Generate a sample of 100 fair coin flips and calculate the sample mean.
"""
# Sample mean from a generated sample of 100 fair coin flips
sample_of_100_flips = binom.rvs(n=1, p=0.5, size=100)
sample_mean_100_flips = describe(sample_of_100_flips).mean
print(sample_mean_100_flips)

#2 Generate a sample of 1,000 fair coin flips and calculate the sample mean.
# Sample mean from a generated sample of 1,000 fair coin flips
sample_mean_1000_flips = describe(binom.rvs(n=1, p=0.5, size=1000)).mean
print(sample_mean_1000_flips)

#3 Generate a sample of 2,000 fair coin flips and calculate the sample mean.
# Sample mean from a generated sample of 2,000 fair coin flips
sample_mean_2000_flips = describe(binom.rvs(n=1, p=0.5, size=2000)).mean
print(sample_mean_2000_flips)
