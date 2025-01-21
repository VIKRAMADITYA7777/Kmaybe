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

# Team selection
batting_team = st.selectbox("Select the Batting Team", 
                            ["Select", "India", "Australia", "England", "South Africa", "New Zealand", "Pakistan", "Sri Lanka", "Bangladesh"])
bowling_team = st.selectbox("Select the Bowling Team", 
                            ["Select", "India", "Australia", "England", "South Africa", "New Zealand", "Pakistan", "Sri Lanka", "Bangladesh"])

# Numeric inputs for match details
overs = st.text_input("Enter Overs Completed (0 to 50)", value="")
runs = st.text_input("Enter Runs Scored So Far", value="")
wickets = st.text_input("Enter Wickets Lost So Far (0 to 10)", value="")

# Validation function
def validate_inputs():
    if batting_team == "Select" or bowling_team == "Select":
        st.error("Please select both Batting and Bowling teams.")
        return False
    if batting_team == bowling_team:
        st.error("Batting and Bowling teams cannot be the same.")
        return False
    try:
        overs_val = float(overs)
        if overs_val < 0 or overs_val > 50:
            st.error("Overs must be between 0 and 50.")
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

    return True

# Predict score button
if st.button("Predict Score"):
    if validate_inputs():
        # Prepare input data for prediction
        # Match the input feature names exactly with the trained model's feature names
        input_data = pd.DataFrame({
            "batting_team": [batting_team],
            "bowling_team": [bowling_team],
            "overs": [float(overs)],
            "runs": [int(runs)],
            "wickets": [int(wickets)],
        })

        # Ensure all columns in `input_data` are the same as in the training data
        try:
            predicted_score = model.predict(input_data)[0]
            st.success(f"The predicted final score is: {predicted_score}")
        except ValueError as e:
            st.error(f"Error during prediction: {e}")
            st.error("Ensure the feature names and input data format match the model's requirements.")
