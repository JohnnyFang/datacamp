"""
Plotting the sample mean

Now let's plot the sample mean, so you can see more clearly how it evolves as more data becomes available.

For this exercise we'll again use the sample you generated earlier, which is available in the sample variable. The binom object and describe() function have already been imported for you from scipy.stats, and matplotlib.pyplot is available as plt.
"""
# Calculate sample mean and store it on averages array
averages = []
for i in range(2, 251):
    averages.append(describe(sample[0:i]).mean)

# Add population mean line and sample mean plot
plt.axhline(binom.mean(n=1, p=0.505), color='red')
plt.plot(averages, '-')

# Add legend
plt.legend(("Population mean","Sample mean"), loc='upper right')
plt.show()
