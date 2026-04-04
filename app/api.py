from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Load the retrained pipeline
pipeline = joblib.load("DiabetesPipeline.joblib")

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

# Helper: convert inputs into numeric format for the model
def encode_inputs(patient: Patient):
    return [[
        int(patient.age.split("-")[0]) if "-" in patient.age else 65,  # convert age range to number
        1 if patient.gender == "Male" else 0,
        1 if patient.family_history == "Yes" else 0,
        1 if patient.blood_pressure == "Yes" else 0,
        1 if patient.activity == "Yes" else 0,
        patient.bmi,
        patient.glucose
    ]]

@app.get("/")
def root():
    return {"message": "API is running"}

@app.post("/predict")
def predict(patient: Patient):
    data = encode_inputs(patient)
    prediction = pipeline.predict(data)[0]
    return {"diabetes_risk": int(prediction)}
