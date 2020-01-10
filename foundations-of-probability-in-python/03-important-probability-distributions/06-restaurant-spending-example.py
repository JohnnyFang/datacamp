"""
Restaurant spending example

Let's go back to the example of the restaurant chain that has been collecting data about customer spending. Recall that the data shows that the spending is approximately normally distributed, with a mean of 3.15 and a standard deviation of 1.5 per customer, as pictured in the plot.

Spending distribution

We can use the already imported norm object from scipy.stats to answer several questions about customer spending at this restaurant chain.

Instructions 1/4
    1. What is the probability that a customer will spend less than $3?
"""
# Probability of spending less than $3
spending = norm.cdf(3, loc=3.15, scale=1.5)
print(spending)

"""
Instructions 2/4
    2. is the probability that a customer will spend more than $5?
"""
# Probability of spending more than $5
spending = norm.sf(5, loc=3.15, scale=1.5)
print(spending)

"""
Instructions 3/4
    3. What is the probability that a customer will spend more than $2.15 and less than $4.15?
"""
# Probability of spending more than $2.15 and less than $4.15
spending_4 = norm.cdf(4.15, loc=3.15, scale=1.5)
spending_2 = norm.cdf(2.15, loc=3.15, scale=1.5)
print(spending_4 - spending_2)

"""
Instructions 4/4
    4. What is the probability that a customer will spend less than $2.15 or more than $4.15?
"""
# Probability of spending less than $2.15 or more than $4.15
spending_2 = norm.cdf(2.15, loc=3.15, scale=1.5)
spending_over_4 = norm.sf(4.15, loc=3.15, scale=1.5)
print(spending_2 + spending_over_4)
