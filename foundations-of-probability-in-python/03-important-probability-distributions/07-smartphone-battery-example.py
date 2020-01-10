"""
Smartphone battery example

One of the most important things to consider when buying a smartphone is how long the battery will last.

Suppose the period of time between charges can be modeled with a normal distribution with a mean of 5 hours and a standard deviation of 1.5 hours.

A friend wants to buy a smartphone and is asking you the following questions.

Instructions 1/3
    1. What is the probability that the battery will last less than 3 hours?
"""

# Probability that battery will last less than 3 hours
less_than_3h = norm.cdf(3, loc=5, scale=1.5)
print(less_than_3h)


"""What is the probability that the battery will last more than 3 hours?"""
# Probability that battery will last more than 3 hours
more_than_3h = norm.sf(3, loc=5, scale=1.5)
print(more_than_3h)

"""What is the probability that the battery will last between 5 and 7 hours?"""
# Probability that battery will last between 5 and 7 hours
P_less_than_7h = norm.cdf(7, loc=5, scale=1.5)
P_less_than_5h = norm.cdf(5, loc=5, scale=1.5)
print(P_less_than_7h - P_less_than_5h)
