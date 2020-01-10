"""
Plotting normal distributions

A certain restaurant chain has been collecting data about customer spending. The data shows that the spending is approximately normally distributed, with a mean of $3.15 and a standard deviation of $1.50 per customer.

Instructions
    Import norm from scipy.stats, matplotlib.pyplot as plt, and seaborn as sns.
    Generate a normal distribution sample with mean 3.15 and standard deviation 1.5.
    Plot the sample generated.
"""
# Import norm, matplotlib.pyplot, and seaborn
from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sns

# Create the sample using norm.rvs()
sample = norm.rvs(loc=3.15, scale=1.5, size=10000, random_state=13)

# Plot the sample
sns.distplot(sample)
plt.show()
