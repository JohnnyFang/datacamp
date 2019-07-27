"""
Calculate the probability that the engine and gear box both work.
"""
# Individual probabilities
P_Eng_works = 0.99
P_GearB_works = 0.995

# Joint probability calculation
P_both_works = P_Eng_works*P_GearB_works

print(P_both_works)

"""
Calculate the probability that one fails -- either engine or gear box -- but not both.
"""
# Individual probabilities
P_Eng_fails = 0.01
P_Eng_works = 0.99
P_GearB_fails = 0.005
P_GearB_works = 0.995

# Joint probability calculation
P_only_GearB_fails = P_GearB_fails*P_Eng_works
P_only_Eng_fails = P_Eng_fails*P_GearB_works

# Calculate result
P_one_fails = P_only_GearB_fails+P_only_Eng_fails

print(P_one_fails)

"""
What is the probability that either both work or both fail?
"""
# Individual probabilities
P_Eng_fails = 0.01
P_Eng_works = 0.99
P_GearB_fails = 0.005
P_GearB_works = 0.995

# Joint probability calculation
P_EngW_GearBW = P_Eng_works*P_GearB_works
P_EngF_GearBF = P_Eng_fails*P_GearB_fails

# Calculate result
P_fails_or_works = P_EngW_GearBW+P_EngF_GearBF

print(P_fails_or_works)
