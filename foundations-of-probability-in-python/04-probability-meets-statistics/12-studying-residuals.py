"""
Studying residuals

To implement a linear model you must study the residuals, which are the distances between the predicted outcomes and the data.

Three conditions must be met:

    The mean should be 0.
    The variance must be constant.
    The distribution must be normal.

We will work with data of test scores for two schools, A and B, on the same subject. model_A and model_B were fitted with hours_of_study_A and test_scores_A and hours_of_study_B and test_scores_B, respectively.

matplotlib.pyplot has been imported as plt, numpy as np and LinearRegression from sklearn.linear_model.

"""
#   1 Make a scatter of hours_of_study_A and test_scores_A and plot hours_of_study_values_A and the outcomes from model_A.
# Scatterplot of hours of study and test scores
plt.scatter(hours_of_study_A, test_scores_A)

# Plot of hours_of_study_values_A and predicted values
plt.plot(hours_of_study_values_A, model_A.predict(hours_of_study_values_A))
plt.title("Model A", fontsize=25)
plt.show()


#   2  Subtract the predicted values and test_scores_A, then make a scatterplot with hours_of_study_A and residuals_A.
# Calculate the residuals
residuals_A = model_A.predict(hours_of_study_A) - test_scores_A

# Make a scatterplot of residuals of model_A
plt.scatter(hours_of_study_A, residuals_A)

# Add reference line and title and show plot
plt.hlines(0, 0, 30, colors='r', linestyles='--')
plt.title("Residuals plot of Model A", fontsize=25)
plt.show()

#   3  Make a scatter of hours_of_study_B and test_scores_B and plot hours_of_study_values_B and the outcomes from model_B.
# Scatterplot of hours of study and test scores
plt.scatter(hours_of_study_B, test_scores_B)

# Plot of hours_of_study_values_B and predicted values
plt.plot(hours_of_study_values_B, model_B.predict(hours_of_study_values_B))
plt.title("Model B", fontsize=25)
plt.show()


#   4 Subtract the predicted values and test_scores_B, then make a scatterplot with hours_of_study_B and residuals_B.
# Calculate the residuals
residuals_B = model_B.predict(hours_of_study_B) - test_scores_B

# Make a scatterplot of residuals of model_B
plt.scatter(hours_of_study_B, residuals_B)

# Add reference line and title and show plot
plt.hlines(0, 0, 30, colors='r', linestyles='--')
plt.title("Residuals plot of Model B", fontsize=25)
plt.show()
