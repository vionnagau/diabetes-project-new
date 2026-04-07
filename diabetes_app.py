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

# Two-column input layout
col1, col2 = st.columns(2)

with col1:
    age_range = st.selectbox("Age Range", ["20-29","30-39","40-49","50-59","60-69","70+"])
    gender = st.radio("Gender", ["Male","Female"])
    high_bp = st.radio("High Blood Pressure?", ["Yes","No"])
    bmi = st.number_input("BMI (kg/m²)", min_value=10.0, max_value=60.0, step=0.1)

with col2:
    physically_active = st.radio("Physically Active?", ["Yes","No"])
    family_history = st.radio("Family History of Diabetes?", ["Yes","No"])
    glucose = st.number_input("Glucose Level (mg/dL)", min_value=20.0, max_value=200.0, step=0.1)

# Predict button
if st.button("Assess Risk"):
    # Encode categorical inputs
    age_val = int(age_range.split("-")[0]) if "-" in age_range else 70
    gender_val = 1 if gender == "Male" else 0
    family_val = 1 if family_history == "Yes" else 0
    bp_val = 1 if high_bp == "Yes" else 0
    active_val = 1 if physically_active == "Yes" else 0

    # Build DataFrame with exact training column names
    input_dict = {
        "Age": age_val,
        "Gender": gender_val,
        "FamilyHistory": family_val,
        "HighBP": bp_val,
        "Activity": active_val,
        "BMI": bmi,
        "Glucose": glucose
    }
    input_df = pd.DataFrame([input_dict])

    # Predict probability
    prediction = model.predict_proba(input_df)[0][1]
    prob_percent = prediction * 100

    # Display result with spacing and hierarchy
    st.markdown("---")  # separator line for clarity

    if prediction >= 0.5:
        st.error("⚠️ High Risk: Based on the provided metrics, there may be an elevated risk of diabetes.")
    else:
        st.success("✅ Low Risk: Based on the provided metrics, diabetes risk appears to be lower.")

    st.markdown("<br>", unsafe_allow_html=True)  # add spacing
    st.markdown("**Risk Probability:**")         # smaller label
    st.markdown(f"<h2 style='margin-top:0;'> {prob_percent:.1f}% </h2>", unsafe_allow_html=True)  # big bold percentage

    # Disclaimer
    st.info("Important: This assessment is not a medical diagnosis. Please consult healthcare professionals for proper evaluation.")

# Professional footer
st.caption("Built with Streamlit and scikit-learn | Model trained on Pima Indians Diabetes dataset")
