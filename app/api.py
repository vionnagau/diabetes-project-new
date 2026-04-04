from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Load the retrained pipeline
pipeline = joblib.load("DiabetesPipeline.joblib")
print("Pipeline expects:", pipeline.n_features_in_)  # Debug check

app = FastAPI()

# Define input schema
class Patient(BaseModel):
    age: str
    gender: str
    family_history: str
    blood_pressure: str
    activity: str
    bmi: float
    glucose: float

# Convert inputs into DataFrame with correct column names
def encode_inputs(patient: Patient):
    data = pd.DataFrame([{
        "Age": int(patient.age.split("-")[0]) if "-" in patient.age else 65,
        "Gender": patient.gender,              # keep as string
        "FamilyHistory": patient.family_history,  # keep as string
        "BloodPressure": patient.blood_pressure,  # keep as string
        "Activity": patient.activity,          # keep as string
        "BMI": patient.bmi,
        "Glucose": patient.glucose
    }])
    print("DataFrame sent to pipeline:\n", data)
    return data

@app.get("/")
def root():
    return {"message": "API is running"}

@app.post("/predict")
def predict(patient: Patient):
    try:
        data = encode_inputs(patient)
        prediction = pipeline.predict(data)[0]
        return {"diabetes_risk": int(prediction)}
    except Exception as e:
        print("Error during prediction:", e)
        return {"error": str(e)}
