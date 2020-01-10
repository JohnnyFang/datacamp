"""
Generating and plotting Poisson distributions

In the previous exercise, you calculated some probabilities. Now let's plot that distribution.

Recall that on a certain highway turn, there are 2 accidents per day on average. Assuming the number of accidents per day can be modeled as a Poisson random variable, let's plot the distribution.
"""
# Generate a Poisson distribution sample with size=10000 and mu=2.
# Plot the sample generated.
# Import poisson, matplotlib.pyplot, and seaborn
from scipy.stats import poisson
import matplotlib.pyplot as plt
import seaborn as sns

# Create the sample
sample = poisson.rvs(mu=2, size=10000, random_state=13)

# Plot the sample
sns.distplot(sample, kde=False)
plt.show()
