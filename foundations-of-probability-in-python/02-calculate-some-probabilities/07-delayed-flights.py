"""
Delayed flights

A certain airline offers flights departing to New York on Tuesdays and Fridays, but sometimes the flights are delayed:
	         Delayed 	On time 	Total
Tuesday 	      24 	114      	138
Friday 	          11 	127        	138
Total 	          35 	241     	276

At the bottom of the Delayed column you have a total of 35, which means there were 35 delayed flights out of the total of 276 departures in the sample. Of these, 24 were on Tuesday and 11 on Friday.

Given the table, answer the following questions:
"""

#  What is the probability of a flight being on time?
# Needed quantities
On_time = 241
Total_departures = 276

# Probability calculation
P_On_time = 241/276

print(P_On_time)

#  Given the probability that it is on time in the variable P_On_time, what is the probability of a flight being delayed?
# Needed quantities
P_On_time = 241 / 276

# Probability calculation
P_Delayed = (35/276)

print(P_Delayed)

#  Given that it's Tuesday, what is the probability of a flight being delayed (P(Delayed|Tuesday))?
# Needed quantities
Delayed_on_Tuesday = 24
On_Tuesday = 138

# Probability calculation
P_Delayed_g_Tuesday = Delayed_on_Tuesday/On_Tuesday

print(P_Delayed_g_Tuesday)

#  Given that it's Friday, what is the probability of a flight being delayed (P(Delayed|Friday))?

# Needed quantities
Delayed_on_Friday = 11
On_Friday = 138

# Probability calculation
P_Delayed_g_Friday = Delayed_on_Friday/On_Friday

print(P_Delayed_g_Friday)

# Probability calculations in a table involve restricting the sample space to the appropriate column or row and comparing the value you are interested in with the total number of cases in that particular column or row.
