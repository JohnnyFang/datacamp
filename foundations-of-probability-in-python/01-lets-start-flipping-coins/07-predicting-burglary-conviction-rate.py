"""
Predicting burglary conviction rate

There are many situations that can be modeled with only two outcomes: success or failure. This exercise presents a situation that can be modeled with a binomial distribution and gives you the opportunity to calculate probabilities using binom.pmf(), binom.cdf(), and binom.sf().

The binom object from scipy.stats has been loaded for your convenience.

Imagine that in your town there are many crimes, including burglaries, but only 20% of them get solved. Last week, there were 9 burglaries. Answer the following questions.

Instructions 1/4
    1 What is the probability of solving exactly 4 of the 9 total burglaries?
"""
# What is the probability of solving 4 burglaries?
four_solved = binom.pmf(k=4, n=9, p=0.2)
print(four_solved)

## What is the probability of solving more than 3 burglaries?
more_than_three_solved = binom.sf(k=3, n=9, p=0.2)
print(more_than_three_solved)

# What is the probability of solving exactly 2 or 3 of the 9 burglaries?
# What is the probability of solving 2 or 3 burglaries?
two_or_three_solved = binom.pmf(k=2, n=9, p=0.2) + binom.pmf(k=3, n=9, p=0.2)
print(two_or_three_solved)

# What is the probability of solving 1 or fewer or 8 or more burglaries?
tail_probabilities = binom.cdf(k=1, n=9, p=0.2) + binom.sf(k=7, n=9, p=0.2)
print(tail_probabilities)
