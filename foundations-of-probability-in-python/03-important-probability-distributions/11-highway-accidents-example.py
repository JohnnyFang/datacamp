"""
On a certain turn on a very busy highway, there are 2 accidents per day. Let's assume the number of accidents per day can be modeled as a Poisson random variable
For your convenience, the poisson object has already been imported from the scipy.stats library.

Aiming to improve road safety, the transportation agency of the regional government has assigned you the following tasks.

"""
# 1  Determine and print the probability of there being 5 accidents on any day.
# Import the poisson object
from scipy.stats import poisson

# Probability of 5 accidents any day
P_five_accidents = poisson.pmf(k=5, mu=2)

# Print the result
print(P_five_accidents)


# 2 Determine and print the probability of having 4 or 5 accidents on any day.
# Import the poisson object
from scipy.stats import poisson

# Probability of having 4 or 5 accidents on any day
P_less_than_6 = poisson.cdf(k=5, mu=2)
P_less_than_3 = poisson.cdf(k=3, mu=2)

# Print the result
print(P_less_than_6 - P_less_than_3)


# 3 Determine and print the probability of having more than 3 accidents on any day.
# Import the poisson object
from scipy.stats import poisson

# Probability of more than 3 accidents any day
P_more_than_3 = poisson.sf(k=3, mu=2)

# Print the result
print(P_more_than_3)

# 4  Determine and print the number of accidents that is likely to happen with 0.75 probability.

# Import the poisson object
from scipy.stats import poisson

# Number of accidents with 0.75 probability
accidents = poisson.ppf(q=0.75, mu=2)

# Print the result
print(accidents)
