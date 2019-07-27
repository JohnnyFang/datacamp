#In this exercise, you'll use the following deck of cards to calculate some probabilities in each step:

"""Calculate the probability of not getting an Ace."""
# Ace probability
P_Ace = 4/52

# Not Ace probability
P_not_Ace = 48/52

print(P_not_Ace)

""" Calculate the probability of getting a red card."""
# Figure probabilities
P_Hearts = 13/52
P_Diamonds = 13/52

# Probability of red calculation
P_Red = P_Hearts + P_Diamonds

print(P_Red)

"""Calculate the probability of getting a Jack or a spade."""
# Figure probabilities
P_Jack = 4/52
P_Spade = 13/52

# Joint probability
P_Jack_n_Spade = P_Jack * P_Spade

# Probability of Jack or spade
P_Jack_or_Spade = P_Jack + P_Spade - 1/52

print(P_Jack_or_Spade)

"""Calculate the probability of getting a King or a Queen."""
# Figure probabilities
P_King = 4/52
P_Queen = 4/52

# Joint probability
P_King_n_Queen = 0

# Probability of King or Queen
P_King_or_Queen = P_King+P_Queen

print(P_King_or_Queen)
# Excellent job! To calculate the probability of A or B you just need to consider whether the events overlap. Be careful, and consider each case.
