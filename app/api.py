from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load pipeline
pipeline = joblib.load("DiabetesPipeline.joblib")

# Define input schema
class Patient(BaseModel):
    glucose: float
    blood_pressure: float
    bmi: float
    age: int

# Create FastAPI app
app = FastAPI()

@app.post("/predict")
def predict(patient: Patient):
    data = np.array([[patient.glucose, patient.blood_pressure, patient.bmi, patient.age]])
    prediction = pipeline.predict(data)[0]
    probability = pipeline.predict_proba(data)[0][prediction]
    return {"prediction": int(prediction), "probability": round(float(probability), 2)}

@app.get("/")
def root():
    return {"message": "API is running"}
