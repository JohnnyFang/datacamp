"""
Swine flu blood test

You go to the doctor about a strong headache. The doctor randomly selects you for a blood test for swine flu, which is suspected to affect 1 in 9,000 people in your city. The accuracy of the test is 99%,
meaning that the probability of a false positive is 1%. The probability of a false negative is zero.

Given that you test positive, answer the following questions.
"""
# What is the probability that you have swine flu?
# Individual probabilities & conditional probabilities
P_Swine_flu = 1/9000
P_no_Swine_flu = 1 - P_Swine_flu
P_Positive_g_Swine_flu = 1
P_Positive_g_no_Swine_flu = 0.01

# Probability of Positive
P_Positive = P_Swine_flu*P_Positive_g_Swine_flu + P_no_Swine_flu*P_Positive_g_no_Swine_flu

# Bayes' rule for P(Swine_flu|Positive)
P_Swine_flu_g_Positive = P_Swine_flu*P_Positive_g_Swine_flu/P_Positive

print(P_Swine_flu_g_Positive)

#  You went to Miami and 1 in 350 people came back with swine flu. Calculate the new probability that you'll test positive.
# Individual probabilities & conditional probabilities
P_Swine_flu = 1./350
P_no_Swine_flu = 1 - P_Swine_flu
P_Positive_g_Swine_flu = 1
P_Positive_g_no_Swine_flu = 0.01

# Probability of Positive
P_Positive = P_Swine_flu*P_Positive_g_Swine_flu + P_no_Swine_flu*P_Positive_g_no_Swine_flu

# Bayes' rule for P(Swine_flu|Positive)
P_Swine_flu_g_Positive = P_Swine_flu*P_Positive_g_Swine_flu/P_Positive

print(P_Swine_flu_g_Positive)

# If the probability of a false positive is 2%, what is the new probability that you have swine flu after your vacation?

# Individual probabilities & conditional probabilities
P_Swine_flu = 1/350
P_no_Swine_flu = 1 - P_Swine_flu
P_Positive_g_Swine_flu = 1
P_Positive_g_no_Swine_flu = 0.02

# Probability of Positive
P_Positive = P_Swine_flu * P_Positive_g_Swine_flu + P_no_Swine_flu * P_Positive_g_no_Swine_flu

# Bayes' rule for P(Swine_flu|Positive)
P_Swine_flu_g_Positive = (P_Swine_flu * P_Positive_g_Swine_flu) / P_Positive

print(P_Swine_flu_g_Positive)
