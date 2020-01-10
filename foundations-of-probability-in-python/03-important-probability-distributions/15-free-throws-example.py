"""
Free throws example

Suppose you know that a basketball player has a 0.3 probability of scoring a free throw. What is the probability of them missing with the first throw and scoring with the second?
"""
# Import geom from scipy.stats
from scipy.stats import geom

# Probability of missing first and scoring on second throw
probability = geom.pmf(k=2, p=0.3)

# Print the result
print(probability)
