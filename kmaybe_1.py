import streamlit as st
import pandas as pd
import pickle

# Load the trained model
try:
    model = pickle.load(open("cricket_score_predictor.pkl", "rb"))
except FileNotFoundError:
    st.error("Model file not found. Please ensure 'cricket_score_predictor.pkl' is in the correct directory.")
    st.stop()

# App title
st.title("Cricket Score Predictor")

# Input fields
st.header("Enter Match Details")

# Numeric inputs for match details
overs = st.text_input("Enter Overs Completed (0 to 50)", value="")
runs = st.text_input("Enter Runs Scored So Far", value="")
wickets = st.text_input("Enter Wickets Lost So Far (0 to 10)", value="")
runs_last_5 = st.text_input("Enter Runs Scored in Last 5 Overs", value="")
wickets_last_5 = st.text_input("Enter Wickets Lost in Last 5 Overs (0 to 10)", value="")
total = st.text_input("Enter Total Possible Overs (e.g., 50 for ODIs)", value="")

# Validation function
def validate_inputs():
    try:
        overs_val = float(overs)
        if overs_val < 0 or overs_val > float(total):
            st.error("Overs must be between 0 and the total possible overs.")
            return False
    except ValueError:
        st.error("Please enter a valid number for Overs.")
        return False

    try:
        runs_val = int(runs)
        if runs_val < 0:
            st.error("Runs cannot be negative.")
            return False
    except ValueError:
        st.error("Please enter a valid number for Runs.")
        return False

    try:
        wickets_val = int(wickets)
        if wickets_val < 0 or wickets_val > 10:
            st.error("Wickets must be between 0 and 10.")
            return False
    except ValueError:
        st.error("Please enter a valid number for Wickets.")
        return False

    try:
        runs_last_5_val = int(runs_last_5)
        if runs_last_5_val < 0:
            st.error("Runs in last 5 overs cannot be negative.")
            return False
    except ValueError:
        st.error("Please enter a valid number for Runs in Last 5 Overs.")
        return False

    try:
        wickets_last_5_val = int(wickets_last_5)
        if wickets_last_5_val < 0 or wickets_last_5_val > 10:
            st.error("Wickets lost in last 5 overs must be between 0 and 10.")
            return False
    except ValueError:
        st.error("Please enter a valid number for Wickets in Last 5 Overs.")
        return False

    try:
        total_val = int(total)
        if total_val <= 0:
            st.error("Total possible overs must be a positive number.")
            return False
    except ValueError:
        st.error("Please enter a valid number for Total Possible Overs.")
        return False

    return True

# Predict score button
if st.button("Predict Score"):
    if validate_inputs():
        # Prepare input data for prediction
        input_data = pd.DataFrame({
            "overs": [float(overs)],
            "runs": [int(runs)],
            "wickets": [int(wickets)],
            "runs_last_5": [int(runs_last_5)],
            "wickets_last_5": [int(wickets_last_5)],
            "total": [int(total)],
        })

        # Make prediction
        try:
            predicted_score = model.predict(input_data)[0]
            st.success(f"The predicted final score is: {predicted_score}")
        except ValueError as e:
            st.error(f"Error during prediction: {e}")
            st.error("Ensure the feature names and input data format match the model's requirements.")
