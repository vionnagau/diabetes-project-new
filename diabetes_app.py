import numpy as np
import streamlit as st
from huggingface_hub import hf_hub_download
import joblib

# Load the trained model from Hugging Face Hub
try:
    model_path = hf_hub_download(repo_id="vionnagau/diabetes-model", filename="Diabetesmodel.pkl")
    model = joblib.load(model_path)
except Exception as e:
    st.error(f"Model could not be loaded: {e}")
    st.stop()

st.title("🩺 AI Diabetes Risk Assessment")

# Input fields
glucose = st.number_input("Glucose (mg/dL)", min_value=20.0, max_value=200.0, step=0.1)
bp = st.number_input("Blood Pressure (mmHg)", min_value=30.0, max_value=150.0, step=0.1)
bmi = st.number_input("BMI (kg/m²)", min_value=10.0, max_value=60.0, step=0.1)
age = st.number_input("Age (years)", min_value=1, max_value=120, step=1)

# Predict button
if st.button("Predict"):
    input_data = np.array([[glucose, bp, bmi, age]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ You are likely to have diabetes.")
    else:
        st.success("✅ You are not likely to have diabetes.")
