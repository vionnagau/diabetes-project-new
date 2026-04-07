import numpy as np
import streamlit as st
from huggingface_hub import hf_hub_download
import joblib

# Load model
try:
    model_path = hf_hub_download(repo_id="vionnagau/diabetes-model", filename="Diabetesmodel.pkl")
    model = joblib.load(model_path)
except Exception as e:
    st.error(f"Model could not be loaded: {e}")
    st.stop()

st.title("🩺 Diabetes Risk Assessment")

# Inputs
age_range = st.selectbox("Age Range", ["20-29","30-39","40-49","50-59","60-69","70+"])
high_bp = st.radio("High Blood Pressure?", ["Yes","No"])
gender = st.radio("Gender", ["Male","Female"])
physically_active = st.radio("Physically Active?", ["Yes","No"])
family_history = st.radio("Family History of Diabetes?", ["Yes","No"])
bmi = st.number_input("BMI (kg/m²)", min_value=10.0, max_value=60.0, step=0.1)
glucose = st.number_input("Glucose Level (mg/dL)", min_value=20.0, max_value=200.0, step=0.1)

# Predict button
if st.button("Assess Risk"):
    # Encode categorical inputs into numeric features
    age_val = int(age_range.split("-")[0])  # crude encoding: lower bound of range
    bp_val = 1 if high_bp == "Yes" else 0
    gender_val = 1 if gender == "Male" else 0
    active_val = 1 if physically_active == "Yes" else 0
    family_val = 1 if family_history == "Yes" else 0

    input_data = np.array([[age_val, bp_val, gender_val, active_val, family_val, bmi, glucose]])
    prediction = model.predict_proba(input_data)[0][1]  # probability of diabetes

    if prediction >= 0.5:
        st.error(f"⚠️ High Risk: Probability {prediction*100:.1f}%")
    else:
        st.success(f"✅ Low Risk: Probability {prediction*100:.1f}%")
