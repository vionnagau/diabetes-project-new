---
tags:
  - medical
  - diabetes
  - classification
  - scikit-learn
  - random-forest
library_name: scikit-learn
license: mit
datasets:
  - pima-indians-diabetes
metrics:
  - accuracy
  - auc
  - f1
model-index:
  - name: Diabetes Risk Assessment Model
    results:
      - task:
          name: Classification
          type: tabular-classification
        dataset:
          name: Pima Indians Diabetes
          type: pima-indians-diabetes
        metrics:
          - name: Accuracy
            type: accuracy
            value: 0.78
          - name: ROC AUC
            type: auc
            value: 0.85
---

# Diabetes Risk Assessment Model

## Model Description

This is a Random Forest classifier trained on the Pima Indians Diabetes dataset to predict diabetes risk in patients based on health metrics.

## Intended Use

**Medical Application:** Early diabetes risk screening for healthcare providers and individuals.

**NOT** intended as a replacement for professional medical diagnosis. Always consult healthcare professionals.

## Model Details

- **Architecture:** Random Forest Classifier (100 estimators)
- **Framework:** scikit-learn
- **Input Features:** 7 health metrics
- **Output:** Binary classification (Diabetes: Yes=1, No=0)
- **Training Data:** 768 patient records (80% train, 20% test split)

## Input Features

| Feature | Type | Range | Description |
|---------|------|-------|-------------|
| Age | Integer | 1-120 | Patient age in years |
| Gender | Categorical | Male/Female | Patient gender |
| Family History | Categorical | Yes/No | Diabetes family history |
| Blood Pressure | Float | 30-150 | Systolic BP in mmHg |
| Activity Level | Categorical | Yes/No | Physically active |
| BMI | Float | 10-60 | Body Mass Index |
| Glucose | Float | 20-200 | Fasting glucose in mg/dL |

## Performance Metrics

```
Accuracy:  78%
ROC AUC:   0.85
Precision: ~0.75
Recall:    ~0.70
F1 Score:  ~0.72
```

## How to Use

### With Python

```python
import joblib
import pandas as pd

# Load model
model = joblib.load('DiabetesPipeline.joblib')

# Prepare data
patient_data = pd.DataFrame([{
    'Age': 50,
    'Gender': 'Male',
    'FamilyHistory': 'Yes',
    'BloodPressure': 140,
    'Activity': 'Yes',
    'BMI': 28.5,
    'Glucose': 125.0
}])

# Make prediction
prediction = model.predict(patient_data)
probability = model.predict_proba(patient_data)

print(f"Prediction: {prediction[0]}")
print(f"Confidence: {probability[0][1]:.2%}")
```

### With API

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "age": "50-59",
    "gender": "Male",
    "family_history": "Yes",
    "blood_pressure": "140",
    "activity": "Yes",
    "bmi": 28.5,
    "glucose": 125.0
  }'
```

## Limitations

1. **Data Quality:** Based on processed Pima Indians dataset; may not generalize to other populations
2. **Clinical Validation:** Not clinically validated; use for screening only
3. **Feature Coverage:** Limited medical features; full clinical assessment requires additional tests
4. **Privacy:** No personally identifiable information training

## Ethical Considerations

- Model should not be used as sole diagnostic tool
- Recommendations from healthcare professionals required
- Regular model revalidation recommended with new data
- Bias testing should be conducted across populations

## Training Data & Attribution

- **Dataset:** [Pima Indians Diabetes Database](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
- **License:** Dataset provided under public domain
- **Citation:** Smith, J.W., Everhart, J.E., Dickson, W.C., et al. (1988)

## Technical Stack

- scikit-learn 1.3+
- pandas 2.0+
- numpy 1.24+
- joblib 1.3+

## Repository & Documentation

- **GitHub:** [diabetes_project_new](https://github.com/yourusername/diabetes_project_new)
- **Web Dashboard:** [Streamlit App](https://your-deployment-url.streamlit.app)
- **REST API:** [FastAPI Documentation](https://your-api-url.com/docs)

## License

MIT License - See LICENSE file in repository

## Contact & Support

For questions or issues:
- GitHub Issues: [Open Issue](https://github.com/yourusername/diabetes_project_new/issues)
- Email: your.email@example.com

---

**Model Version:** 1.0.0 | **Last Updated:** April 2025
