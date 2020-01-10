"""
ATM example

If you know how many specific events occurred per unit of measure, you can assume that the distribution of the random variable follows a Poisson distribution to study the phenomenon.

Consider an ATM (automatic teller machine) at a very busy shopping mall. The bank wants to avoid making customers wait in line to use the ATM. It has been observed that the average number of customers making withdrawals between 10:00 a.m. and 10:05 a.m. on any given day is 1.

As a data analyst at the bank, you are asked what the probability is that the bank will need to install another ATM to handle the load.

To answer the question, you need to calculate the probability of getting more than one customer during that time period.
"""
# Import poisson from scipy.stats
from scipy.stats import poisson

# Probability of more than 1 customer
probability = poisson.sf(k=1, mu=1)

# Print the result
print(probability)
