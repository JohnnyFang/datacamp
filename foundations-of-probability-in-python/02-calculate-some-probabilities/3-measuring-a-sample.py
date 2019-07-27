"""
Measuring a sample

Let's work with a sample of coin flips to calculate some probabilities. You will calculate absolute and relative frequency and check the theoretical value from the distribution of the sample data.

The array sample_of_two_coin_flips has 1,000 experiments, each consisting of two fair coin flips. For each experiment, we record the number of heads out of the two coin flips: 0, 1, or 2.

We've preloaded the binom object and the find_repeats() and relfreq() methods from the scipy.stats library for you. You'll need these to calculate the probabilities in this exercise.
Instructions 1/3
    From the provided samples in sample_of_two_coin_flips, get the probability of having 2 heads out of the 1,000 trials.
"""
# Count how many times you got 2 heads from the sample data
count_2_heads = find_repeats(sample_of_two_coin_flips).counts[2]

# Divide the number of heads by the total number of draws
prob_2_heads = count_2_heads / 1000

# Display the result
print(prob_2_heads)

"""
Calculate the relative frequency from sample_of_two_coin_flips, set numbins as 3, and extract frequency.
"""
# Get the relative frequency from sample_of_two_coin_flips
# Set numbins as 3
# Extract frequency
rel_freq = relfreq(sample_of_two_coin_flips, numbins=3).frequency
print(rel_freq)

"""
Calculate the probability of getting 0, 1, or 2 from a binomial distribution with n=2 and p=0.5.
"""
# Probability of getting 0, 1, or 2 from the distribution
probabilities = binom.pmf([0, 1, 2], n=2, p=0.5)
print(probabilities)
