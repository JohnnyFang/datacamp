"""
Calculating the mean and variance of a sample

Now that you're familiar with working with coin flips using the binom object and calculating the mean and variance, let's try simulating a larger number of coin flips and calculating the sample mean and variance. Comparing this with the theoretical mean and variance will allow you to check if your simulated data follows the distribution you want.

We've preloaded the binom object and the describe() method from scipy.stats for you, as well as creating an empty list called averages to store the mean of the sample variable and a variable called variances to store the variance of the sample variable.

Instructions 1/3
    Inside a loop, create a sample variable with 10 trials of 10 coin flips with 25% probability of getting heads.
"""
for i in range(0, 1500):
    # 10 trials of 10 coin flips with 25% probability of heads
    sample = binom.rvs(n=10, p=0.25, size=10)
    # Mean and variance of the values in the sample variable
    averages.append(describe(sample).mean)
    variances.append(describe(sample).variance)

"""
Instructions 2/3
    Using the describe() function, calculate the mean of the averages array.
    Using the describe() function, calculate the variance of the averages array.
"""
for i in range(0, 1500):
	# 10 draws of 10 coin flips with 25% probability of heads
    sample = binom.rvs(n=10, p=0.25, size=10)
	# Mean and variance of the values in the sample variable
    averages.append(describe(sample).mean)
    variances.append(describe(sample).variance)

# Calculate the mean of the averages variable
print("Mean {}".format(describe(averages).mean))

# Calculate the mean of the variances variable
print("Variance {}".format(describe(variances).mean))

"""
Instructions 3/3
    Using the binom.stats() function, calculate the theoretical mean and variance using 10 and 25% probability of getting heads and compare your results from the previous exercise to the expected values for the mean and variance.
"""
# Calculate the mean and variance
print(binom.stats(n=10, p=0.25))
