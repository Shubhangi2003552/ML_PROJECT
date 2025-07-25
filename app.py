import streamlit as st
import numpy as np
import joblib

# Load the trained model (and scaler if used)
model = joblib.load("best_model.pkl")
# scaler = joblib.load("scaler.pkl")  # Uncomment if used

st.title("🚗 Insurance Claim Fraud Prediction App")

# User inputs
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=18, max_value=100)
driving_license = st.selectbox("Do you have a Driving License?", ["Yes", "No"])
region_code = st.number_input("Region Code", min_value=0.0)
previously_insured = st.selectbox("Previously Insured?", ["Yes", "No"])
vehicle_age = st.selectbox("Vehicle Age", ["< 1 Year", "1-2 Year", "> 2 Years"])
vehicle_damage = st.selectbox("Any Previous Vehicle Damage?", ["Yes", "No"])
annual_premium = st.number_input("Annual Premium (₹)", min_value=1000.0)
policy_channel = st.number_input("Policy Sales Channel", min_value=0.0)
vintage = st.number_input("Vintage (days with company)", min_value=0)

# Convert inputs to numerical format (label encoding like your training)
gender = 1 if gender == "Male" else 0
driving_license = 1 if driving_license == "Yes" else 0
previously_insured = 1 if previously_insured == "Yes" else 0
vehicle_damage = 1 if vehicle_damage == "Yes" else 0

# One-hot encoding for Vehicle_Age
vehicle_age_1_2 = 1 if vehicle_age == "1-2 Year" else 0
vehicle_age_2plus = 1 if vehicle_age == "> 2 Years" else 0

# Combine into array
input_data = np.array([[gender, age, driving_license, region_code,
                        previously_insured, vehicle_damage,
                        annual_premium, policy_channel, vintage,
                        vehicle_age_1_2, vehicle_age_2plus]])

# If you used a scaler:
# input_data = scaler.transform(input_data)

# Predict
if st.button("Predict Fraud"):
    pred = model.predict(input_data)[0]
    if pred == 1:
        st.error("⚠️ Potential Fraudulent Claim Detected")
    else:
        st.success("✅ No Fraud Detected")
