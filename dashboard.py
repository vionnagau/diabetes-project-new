import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load dataset sample
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
column_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
                'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']
df = pd.read_csv(url, header=None, names=column_names)

# Load pipeline
pipeline = joblib.load("DiabetesPipeline.joblib")

st.title("Diabetes Prediction Dashboard")

st.subheader("Dataset Sample")
st.dataframe(df.head())

st.subheader("Patient Input")
glucose = st.slider("Glucose", 0, 200, 120)
blood_pressure = st.slider("Blood Pressure", 0, 122, 70)
bmi = st.slider("BMI", 0, 67, 25)
age = st.slider("Age", 21, 100, 30)

if st.button("Predict"):
    data = np.array([[glucose, blood_pressure, bmi, age]])
    prediction = pipeline.predict(data)[0]
    probability = pipeline.predict_proba(data)[0][prediction]
    st.write("Prediction:", "Diabetic" if prediction == 1 else "Not Diabetic")
    st.write("Probability:", round(float(probability), 2))
