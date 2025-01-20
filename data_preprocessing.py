# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 17:37:27 2025

@author: HP
"""

# Updated data_preprocessing.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the dataset
data = pd.read_csv("re_cricketdata.csv")

# Features and target variable
X = data[['overs', 'runs', 'wickets', 'runs_last_5', 'wickets_last_5']]
y = data['total']

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Save processed data for later use
pd.DataFrame(X_train).to_csv("X_train.csv", index=False)
pd.DataFrame(X_test).to_csv("X_test.csv", index=False)
pd.DataFrame(y_train).to_csv("y_train.csv", index=False)
pd.DataFrame(y_test).to_csv("y_test.csv", index=False)

print("Preprocessing complete and files saved!")
