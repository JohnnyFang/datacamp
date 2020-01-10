"""
Fitting a logistic model

The university studying the relationship between hours of study and outcomes on a given test has provided you with a data set containing the number of hours the students studied and whether they failed or passed the test, and asked you to fit a model to predict future performance.

The data is provided in the variables hours_of_study and outcomes. Use this data to fit a LogisticRegression model. numpy has been imported as np for your convenience.
"""
# Import LogisticRegression
from sklearn.linear_model import LogisticRegression

# sklearn logistic model
model = LogisticRegression(C=1e9)
model.fit(hours_of_study, outcomes)

# Get parameters
beta1 = model.coef_[0][0]
beta0 = model.intercept_[0]

# Print parameters
print(beta1, beta0)
