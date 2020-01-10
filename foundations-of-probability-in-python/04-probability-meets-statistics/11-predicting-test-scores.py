"""
Predicting test scores

With the relationship between the hours of study and the scores that students got on a given test, you already got the parameters of a linear model, slope and intercept. With those parameters, let's predict the test score for a student who studies for 10 hours.

For this exercise, the linregress() function has been imported for you from scipy.stats.


"""
#   1   Predict the test score for 10 hours of study using the provided parameters in slope and intercept, then print the score.
# Get the predicted test score for given hours of study
score = slope*10 + intercept
print('score:', score)


#   2 Now predict the score for 9 hours of study using the parameters in slope and intercept, then print the score.
# Get the predicted test score for given hours of study
score = slope*9 + intercept
print('score:', score)

#   3 Lastly, predict the score for 12 hours of study using the same parameters, and print the score.
# Get the predicted test score for given hours of study
score = slope*12 + intercept
print('score:', score)
