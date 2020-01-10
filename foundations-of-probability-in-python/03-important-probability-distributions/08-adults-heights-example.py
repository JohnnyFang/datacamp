"""
Adults' heights example

The heights of adults aged between 18 and 35 years are normally distributed. For males,
the mean height is 70 inches with a standard deviation of 4. Adult females have a mean
 height of 65 inches with a standard deviation of 3.5. You can see how the heights are distributed in this plot:

Adults heights distribution for male and female

Using the previous information, complete the following exercises.

For your convenience, norm has been imported from the library scipy.stats.

Instructions 1/4
    Print the range of female heights one standard deviation from the mean.
"""
# Values one standard deviation from mean height for females
interval = norm.interval(0.68, loc=65, scale=3.5)
print(interval)

"""Print the value where the tallest males fall with 0.01 probability."""
# Value where the tallest males fall with 0.01 probability
tallest = norm.ppf(0.99, loc=70, scale=4)
print(tallest)

"""Print the probability of being taller than 73 inches for a male and for a female."""
# Probability of being taller than 73 inches for males and females
P_taller_male = norm.sf(73, loc=70, scale=4)
P_taller_female = norm.sf(73, loc=65, scale=3.5)
print(P_taller_male, P_taller_female)

"""Print the probability of being shorter than 61 inches for a male and for a female."""
# Probability of being shorter than 61 inches for males and females
P_shorter_male = norm.cdf(61, loc=70, scale=4)
P_shorter_female = norm.cdf(61, loc=65, scale=3.5)
print(P_shorter_male, P_shorter_female)
