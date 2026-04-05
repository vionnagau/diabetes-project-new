import streamlit as st
import joblib
import pandas as pd

# Load the model
@st.cache_resource
def load_model():
    return joblib.load('DiabetesPipeline.joblib')

model = load_model()

st.title("Diabetes Risk Assessment")

st.markdown("""
This tool helps assess diabetes risk based on health metrics.
**Note:** This is for educational purposes only. Consult healthcare professionals for medical advice.
""")

# Collect user inputs
col1, col2 = st.columns(2)

with col1:
    age = st.selectbox("Age Range", ["18-39", "40-49", "50-59", "60-64", "65+"])
    gender = st.radio("Gender", ["Male", "Female"])
    family_history = st.radio("Family History of Diabetes?", ["Yes", "No"])

with col2:
    blood_pressure = st.radio("High Blood Pressure?", ["Yes", "No"])
    activity = st.radio("Physically Active?", ["Yes", "No"])
    bmi = st.number_input("BMI", 10.0, 60.0, 25.0)
    glucose = st.number_input("Glucose Level (mg/dL)", 20, 300, 100)

if st.button("Assess Risk", type="primary"):
    # Convert inputs to match model expectations
    age_num = int(age.split("-")[0]) if "-" in age else 65

    patient_data = pd.DataFrame([{
        "Age": age_num,
        "Gender": gender,
        "FamilyHistory": family_history,
        "BloodPressure": blood_pressure,
        "Activity": activity,
        "BMI": bmi,
        "Glucose": glucose
    }])

    try:
        prediction = model.predict(patient_data)[0]
        probability = model.predict_proba(patient_data)[0]

        st.subheader("Assessment Result")

        if prediction == 1:
            st.error("⚠️ **High Risk**: Based on the provided metrics, there may be an elevated risk of diabetes.")
            st.metric("Risk Probability", f"{probability[1]:.1%}")
        else:
            st.success("✅ **Low Risk**: Based on the provided metrics, diabetes risk appears low.")
            st.metric("Risk Probability", f"{probability[1]:.1%}")

        st.info("**Important:** This assessment is not a medical diagnosis. Please consult with healthcare professionals for proper evaluation.")

    except Exception as e:
        st.error(f"Assessment error: {str(e)}")

# Footer
st.markdown("---")
st.caption("Built with Streamlit and scikit-learn | Model trained on Pima Indians Diabetes dataset")