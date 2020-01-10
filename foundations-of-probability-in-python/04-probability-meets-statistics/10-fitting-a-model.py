"""
Fitting a model

A university has provided you with data that shows a relationship between the hours of study and the scores that the students get on a given test.

You have access to the data through the variables hours_of_study and scores. Use a linear model to learn from the data.

Instructions

    Import the linregress() function from scipy.stats.
    Fit a linear model using the provided data in the hours_of_study and scores variables.
    Print the parameters.
"""
# Import the linregress() function
from scipy.stats import linregress

# Get the model parameters
slope, intercept, r_value, p_value, std_err = linregress(hours_of_study, scores)

# Print the linear model parameters
print('slope:', slope)
print('intercept:', intercept)
