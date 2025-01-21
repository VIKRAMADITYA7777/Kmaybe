# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 19:15:29 2025

@author: HP
"""

# Updated reapp.py

import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("cricket_score_predictor.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Cricket Score Predictor")

# Input features
overs = st.number_input("Overs Bowled", min_value=0.0, max_value=50.0, step=0.1)
runs = st.number_input("Current Runs", min_value=0, max_value=500, step=1)
wickets = st.number_input("Wickets Lost", min_value=0, max_value=10, step=1)
runs_last_5 = st.number_input("Runs in Last 5 Overs", min_value=0, max_value=100, step=1)
wickets_last_5 = st.number_input("Wickets Lost in Last 5 Overs", min_value=0, max_value=10, step=1)

# Prediction
if st.button("Predict"):
    features = np.array([[overs, runs, wickets, runs_last_5, wickets_last_5]])
    prediction = model.predict(features)
    st.success(f"Predicted Total Score: {round(prediction[0])}")
   
#import streamlit as st
#import pickle
#import numpy as np

# Load the model
#model = pickle.load(open("cricket_score_predictor.pkl", "rb"))

# Streamlit app title
#st.title("Cricket Score Predictor")

# Input fields
#st.header("Enter Match Details")
#batting_team = st.selectbox("Select Batting Team", ['Choose...', 'Team1', 'Team2', 'Team3', 'Team4'])
#bowling_team = st.selectbox("Select Bowling Team", ['Choose...', 'Team1', 'Team2', 'Team3', 'Team4'])
#overs = st.text_input("Enter Overs Completed (e.g., 12.5)")
#runs = st.text_input("Enter Current Runs")
#wickets = st.text_input("Enter Current Wickets")
#runs_in_prev_5 = st.text_input("Enter Runs Scored in Last 5 Overs")
#wickets_in_prev_5 = st.text_input("Enter Wickets Lost in Last 5 Overs")

# Prediction button
#if st.button("Predict Score"):
  #  # Validation logic
  #  if (
  #      batting_team == 'Choose...'
  #      or bowling_team == 'Choose...'
  #      or not overs
  #      or not runs
  #      or not wickets
  #      or not runs_in_prev_5
  #      or not wickets_in_prev_5
  #  ):
   #     st.error("Please fill in all the fields to predict the score!")
   # else:
        # Convert inputs to required format
       # try:
           # overs = float(overs)
          #  runs = int(runs)
         #   wickets = int(wickets)
        #    runs_in_prev_5 = int(runs_in_prev_5)
       #     wickets_in_prev_5 = int(wickets_in_prev_5)

            # Create input array
      #      input_array = np.array([[batting_team, bowling_team, overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5]])

            # Make prediction
     #       prediction = model.predict(input_array)
    #        st.success(f"Predicted Final Score: {int(prediction[0])}")
   #     except ValueError:
  #          st.error("Please enter valid numeric values for overs, runs, wickets, and recent data fields!")

