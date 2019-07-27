"""
Checking the result

Now try generating some samples and calculating the expected value and variance yourself, then using the method provided by binom to check if the sample values match the theoretical values.

The binom object and describe() method from scipy.stats are already loaded, so you can make the calculations.
Instructions
    Calculate the sample mean and variance of the sample variable.
    Calculate the expected value using n and p, and calculate the variance using mean, and 1 - p.
    Use a binom method to get the expected value and variance for 10 coin flips with p=0.3.
"""
sample = binom.rvs(n=10, p=0.3, size=2000)

# Calculate the sample mean and variance from the sample variable
sample_describe = describe(sample)

# Calculate the sample mean
mean = 10*0.3

# Calculate the sample variance
variance = mean*(1-0.3)

# Calculate the sample mean and variance for 10 coin flips with p=0.3
binom_stats = binom.stats(n=10, p=0.3)

print(sample_describe.mean, sample_describe.variance, mean, variance, binom_stats)
