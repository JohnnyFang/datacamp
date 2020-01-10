"""
Passing two tests

Put yourself in the shoes of one of the university students. You have two tests coming up in different subjects, and you're running out of time to study. You want to know how much time you have to study each subject to maximize the probability of passing both tests. Fortunately, there's data that you can use.

For subject A, you already fitted a logistic model in model_A, and for subject B you fitted a model in model_B. As well as preloading LogisticRegression from sklearn.linear_model and numpy as np, expit(), the inverse of the logistic function, has been imported for you from scipy.special.
"""
#   1 Use model_A to predict if you'll pass the test with 6, 7, 8, 9, or 10 hours of study and model_B with 3, 4, 5, or 6.
# Specify values to predict
hours_of_study_test_A = [[6], [7], [8], [9], [10]]

# Pass values to predict
predicted_outcomes_A = model_A.predict(hours_of_study_test_A)
print(predicted_outcomes_A)

# Specify values to predict
hours_of_study_test_B = [[3], [4], [5], [6]]

# Pass values to predict
predicted_outcomes_B = model_B.predict(hours_of_study_test_B)
print(predicted_outcomes_B)


#    2 Get the probability of passing for test A with 8.6 hours of study and test B with 4.7 hours of study.
# Set value in array
value_A = np.asarray(8.6).reshape(-1,1)
# Probability of passing test A with 8.6 hours of study
print("The probability of passing test A with 8.6 hours of study is ", model_A.predict_proba(value_A)[:,1])

# Set value in array
value_B = np.asarray(4.7).reshape(-1,1)
# Probability of passing test B with 4.7 hours of study
print("The probability of passing test B with 4.7 hours of study is ", model_B.predict_proba(value_B)[:,1])


#   3 Calculate the hours you need to study to have 0.5 probability of passing the test using the formula -intercept/slope.
# Print the hours required to have 0.5 probability on model_A
print("Minimum hours of study for test A are ", -model_A.intercept_/model_A.coef_)

# Print the hours required to have 0.5 probability on model_B
print("Minimum hours of study for test B are ", -model_B.intercept_/model_B.coef_)


#   4 Calculate the joint probability of passing test A and test B.
# Probability calculation for each value of study_hours
prob_passing_A = model_A.predict_proba(study_hours_A.reshape(-1,1))[:,1]
prob_passing_B = model_B.predict_proba(study_hours_B.reshape(-1,1))[:,1]

# Calculate the probability of passing both tests
prob_passing_A_and_B = prob_passing_A * prob_passing_B

# Maximum probability value
max_prob = max(prob_passing_A_and_B)

# Position where we get the maximum value
max_position = np.where(prob_passing_A_and_B == max_prob)[0][0]

# Study hours for each test
print("Study {:1.0f} hours for the first and {:1.0f} hours for the second test and you will pass both tests with {:01.2f} probability.".format(study_hours_A[max_position], study_hours_B[max_position], max_prob))

# Nicely done!! When you fit a logistic model you obtain the parameters that are used to calculate probabilities and to predict outcomes. The calculation of probability is done by the model using predict_proba(). Now students have a method to work out how to use the time available in a smart way to pass both tests!
