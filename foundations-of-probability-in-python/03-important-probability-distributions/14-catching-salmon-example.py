"""
Catching salmon example

Every fall the salmon run occurs -- this is the time when salmon swim back upriver from the ocean to spawn.
While swimming back to the upper river (usually to the place where they were spawned), the fish may encounter grizzly bears.
Some of these bears can eat 18 salmon in 3 hours, and they have a 0.0333 probability of success in their attempts to catch a fish.

Grizzly bears catching salmons
We can model a grizzly bear catching salmon with a geometric distribution.

For the following exercises, the geom object from scipy.stats has already been loaded for your convenience.
"""
# 1 Calculate and print the probability that the bear will catch a salmon on its third attempt, after failing two times.
# Getting a salmon on the third attempt
probability = geom.pmf(k=3, p=0.0333)

# Print the result
print(probability)

# 2  Calculate and print the probability that the bear will get a salmon in less than 5 attempts.
# Probability of getting a salmon in less than 5 attempts
probability = geom.cdf(k=4, p=0.0333)

# Print the result
print(probability)

# 3 Calculate and print the probability that the bear will get a salmon in less than 21 attempts.
# Probability of getting a salmon in less than 21 attempts
probability = geom.cdf(k=20, p=0.0333)

# Print the result
print(probability)

# 4 Calculate and print how many attempts the bear has to make to have a 0.9 probability of catching a salmon.
# Attempts for 0.9 probability of catching a salmon
attempts = geom.ppf(q=0.9, p=0.0333)

# Print the result
print(attempts)
