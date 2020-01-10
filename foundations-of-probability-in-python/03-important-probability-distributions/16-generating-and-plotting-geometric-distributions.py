"""
Generating and plotting geometric distributions

In sports it is common for players to make multiple attempts to score points for themselves or their teams. Each single attempt can have two possible outcomes, scoring or not scoring. Those situations can be modeled with geometric distributions. With scipy.stats you can generate samples using the rvs() function for each distribution.

Consider the previous example of a basketball player who scores free throws with a probability of 0.3. Generate a sample, and plot it.

numpy has been imported for you with the standard alias np.
Generate a sample with size=10000 from a geometric distribution with a probability of success of 0.3.
Plot the sample generated.
"""
# Import geom, matplotlib.pyplot, and seaborn
from scipy.stats import geom
import matplotlib.pyplot as plt
import seaborn as sns

# Create the sample
sample = geom.rvs(p=0.3, size=10000, random_state=13)

# Plot the sample
sns.distplot(sample, bins = np.linspace(0,20,21), kde=False)
plt.show()
