# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 19:08:34 2025

@author: HP
"""

# Updated visualization.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load actual and predicted values
y_test = pd.read_csv("y_test.csv").values.ravel()
y_pred = pd.read_csv("predictions.csv")['Predicted'].values

# Scatter plot for actual vs predicted scores
sns.scatterplot(x=y_test, y=y_pred)
plt.xlabel("Actual Scores")
plt.ylabel("Predicted Scores")
plt.title("Actual vs Predicted Scores")
plt.show()

# Distribution of errors
errors = y_test - y_pred
sns.histplot(errors, kde=True)
plt.title("Distribution of Prediction Errors")
plt.xlabel("Error (Actual - Predicted)")
plt.ylabel("Frequency")
plt.show()
