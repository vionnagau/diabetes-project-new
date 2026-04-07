import streamlit as st
import pandas as pd
import joblib
from huggingface_hub import hf_hub_download

# Load model from Hugging Face Hub
try:
    model_path = hf_hub_download(
        repo_id="vionnagau/diabetes-model",
        filename="Diabetesmodel.pkl"
    )
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
    age_val = int(age_range.split("-")[0]) if "-" in age_range else 70
    bp_val = 1 if high_bp == "Yes" else 0
    gender_val = 1 if gender == "Male" else 0
    active_val = 1 if physically_active == "Yes" else 0
    family_val = 1 if family_history == "Yes" else 0

    # Build DataFrame with correct column names
    input_dict = {
        "Age": age_val,
        "HighBP": bp_val,
        "Gender": gender_val,
        "PhysicallyActive": active_val,
        "FamilyHistory": family_val,
        "BMI": bmi,
        "Glucose": glucose
    }
    input_df = pd.DataFrame([input_dict])

    # Predict probability
    prediction = model.predict_proba(input_df)[0][1]

    # Display result
    if prediction >= 0.5:
        st.error(f"⚠️ High Risk: Probability {prediction*100:.1f}%")
    else:
        st.success(f"✅ Low Risk: Probability {prediction*100:.1f}%")
