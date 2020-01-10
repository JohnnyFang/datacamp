"""
Calculating the sample mean

Now you can calculate the sample mean for this generated sample by taking some elements from the sample.

Using the sample variable you just created, you'll calculate the sample means of the first 10, 50, and 250 samples.

The binom object and describe() method from scipy.stats have been imported for your convenience.
"""
# 1
# Print the sample mean of the first 10 samples
print(describe(sample[0:10]).mean)

# 2
# Print the sample mean of the first 50 samples
print(describe(sample[0:50]).mean)

# 3
# Print the sample mean of the first 250 samples
print(describe(sample[0:250]).mean)
