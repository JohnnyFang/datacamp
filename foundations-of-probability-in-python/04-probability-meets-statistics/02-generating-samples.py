"""
Generating a sample

A hospital's planning department is investigating different treatments for newborns.
As a data scientist you are hired to simulate the sex of 250 newborn children,
and you are told that on average 50.50% are males.

"""
# Import the binom object
from scipy.stats import binom

# Generate a sample of 250 newborn children
sample = binom.rvs(n=2, p=0.505, size=250, random_state=42)

# Show the sample values
print(sample)
