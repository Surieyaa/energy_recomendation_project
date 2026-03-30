
import streamlit as st
import numpy as np
import pandas as pd
import joblib


model = joblib.load("energy_model.pkl")
scaler = joblib.load("scaler.pkl")
features = joblib.load("features.pkl")

# ==============================
# UI TITLE
# ==============================
st.title("⚡ Energy Consumption Prediction App")

st.write("Enter the details below to predict energy usage")

# ==============================
# USER INPUTS
# ==============================

temperature = st.slider("Temperature (°C)", 0, 50, 30)
humidity = st.slider("Humidity (%)", 0, 100, 60)

hour = st.slider("Hour of Day", 0, 23, 12)
day = st.slider("Day", 1, 31, 15)
month = st.slider("Month", 1, 12, 6)
weekday = st.slider("Weekday (0=Mon)", 0, 6, 3)

# Lag inputs
lag1 = st.number_input("Last Hour Energy (Lag1)", value=500.0)
lag2 = st.number_input("2nd Last Hour (Lag2)", value=480.0)
lag3 = st.number_input("3rd Last Hour (Lag3)", value=470.0)

# Rolling features
rolling_mean = (lag1 + lag2 + lag3) / 3
rolling_std = np.std([lag1, lag2, lag3])

# ==============================
# PREDICTION BUTTON
# ==============================
if st.button("Predict Energy"):

    # Create input dictionary
    input_dict = {
        "Temperature": temperature,
        "Humidity": humidity,
        "Hour": hour,
        "Day": day,
        "Month": month,
        "Weekday": weekday,
        "Lag1": lag1,
        "Lag2": lag2,
        "Lag3": lag3,
        "Rolling_Mean": rolling_mean,
        "Rolling_Std": rolling_std
    }

    # Convert to DataFrame
    input_df = pd.DataFrame([input_dict])

    # Add missing features (IMPORTANT FIX)
    for col in features:
        if col not in input_df:
            input_df[col] = 0

    # Arrange columns in correct order
    input_df = input_df[features]

    input_scaled = scaler.transform(input_df)

    prediction = model.predict(input_scaled)


    st.success(f"⚡ Predicted Energy Consumption: {prediction[0]:.2f}")

    if prediction[0] > lag1:
        st.warning("⚠️ High energy usage predicted! Reduce AC or lighting usage.")
    else:
        st.info("✅ Energy usage is normal.")