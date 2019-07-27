"""
Contingency table

The following table shows the numbers of red and black cards in a deck that are Aces and non-Aces:
	       Red 	Black 	Total
Ace 	    2 	   2    	4
Non Ace 	24 	   24   	48
Total 	    26    26      	52

The total in the Red column is 26, which means there are 26 red cards in the deck. Of these, 2 are Aces and 24 are non-Aces. There are 52 cards in a deck. Use the values in the table to calculate some conditional probabilities.
"""
# Calculate P(Ace|Red).
# Individual probabilities
P_Red = 26/52
P_Red_n_Ace = 2/52

# Conditional probability calculation
P_Ace_given_Red = P_Red_n_Ace/P_Red

print(P_Ace_given_Red)

#   Calculate P(Black|Ace).\
# Individual probabilities
P_Ace = 4/52
P_Ace_n_Black = 2/52

# Conditional probability calculation
P_Black_given_Ace = P_Ace_n_Black/P_Ace

print(P_Black_given_Ace)

# Calculate P(Non Ace|Black).
# Individual probabilities
P_Black = 26/52
P_Black_n_Non_ace = 24/52

# Conditional probability calculation
P_Non_ace_given_Black = P_Black_n_Non_ace/P_Black

print(P_Non_ace_given_Black)


#  Calculate P(Red|Non Ace).
# Individual probabilities
P_Non_ace = 48/52
P_Non_ace_n_Red = 24/52

# Conditional probability calculation
P_Red_given_Non_ace = P_Non_ace_n_Red/P_Non_ace

print(P_Red_given_Non_ace)
