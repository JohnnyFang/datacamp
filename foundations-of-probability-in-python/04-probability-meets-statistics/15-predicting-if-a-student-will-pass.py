"""
Predicting if students will pass

In the previous exercise you calculated the parameters of the logistic regression model that fits the data of hours of study and test outcomes.

With those parameters you can predict the performance of students based on their hours of study. Use model.predict() to get the outcomes based on the logistic regression.

For your convenience, LogisticRegression has been imported from sklearn.linear_model and numpy has been imported as np.


    Create an array with the values 10, 11, 12, 13, and 14 to predict the outcomes for a test based on those numbers of hours of study.
    Use model.predict() to get the outcomes from the model, and print the outcomes.
    Use model.predict_proba() to get the probability of passing the test with 11 hours of study.

"""
# Specify values to predict
hours_of_study_test = [[10], [11], [12], [13], [14]]

# Pass values to predict
predicted_outcomes = model.predict(hours_of_study_test)
print(predicted_outcomes)

# Set value in array
value = np.asarray(11).reshape(-1,1)
# Probability of passing the test with 11 hours of study
print("Probability of passing test ", model.predict_proba(value)[:,1])
