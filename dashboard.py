import streamlit as st
import requests

st.title("Diabetes Risk Checker")

# Collect user inputs
age = st.selectbox("Age Range", ["18-39", "40-49", "50-59", "60-64", "65+"])
gender = st.radio("Gender", ["Male", "Female"])
family_history = st.radio("Family History of Diabetes?", ["Yes", "No"])
blood_pressure = st.radio("High Blood Pressure?", ["Yes", "No"])
activity = st.radio("Physically Active?", ["Yes", "No"])
bmi = st.number_input("BMI", 0.0, 60.0)
glucose = st.number_input("Glucose Level", 0, 300)

# Send data to API
if st.button("Check Risk"):
    patient = {
        "age": age,
        "gender": gender,
        "family_history": family_history,
        "blood_pressure": blood_pressure,
        "activity": activity,
        "bmi": bmi,
        "glucose": glucose
    }
    response = requests.post("http://localhost:8000/predict", json=patient)
    st.write("Result:", response.json())
