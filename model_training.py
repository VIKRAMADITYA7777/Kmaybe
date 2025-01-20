# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 19:07:52 2025

@author: HP
"""

# Updated model_training.py

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import pickle

# Load processed data
X_train = pd.read_csv("X_train.csv")
X_test = pd.read_csv("X_test.csv")
y_train = pd.read_csv("y_train.csv").values.ravel()
y_test = pd.read_csv("y_test.csv").values.ravel()

# Initialize and train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print(f"Model Evaluation: MAE = {mae}, MSE = {mse}")

# Save the model
with open("cricket_score_predictor.pkl", "wb") as file:
    pickle.dump(model, file)
import pandas as pd

# Assuming y_test and y_pred are defined
predictions_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
predictions_df.to_csv('predictions.csv', index=False)
print("Predictions saved in predictions.csv")

print("Model saved successfully!")
