import requests
import streamlit as st

st.title("Diabetes Risk Checker")

# Collect user input
age = st.number_input("Age", 18, 100)
glucose = st.number_input("Glucose Level", 0, 300)
bmi = st.number_input("BMI", 0.0, 60.0)

if st.button("Check Risk"):
    patient = {"age": age, "glucose": glucose, "bmi": bmi}
    response = requests.post("http://localhost:8000/predict", json=patient)
    st.write("Result:", response.json())
