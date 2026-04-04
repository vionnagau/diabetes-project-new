import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score, confusion_matrix, classification_report
import joblib

# Load dataset (replace with your own if needed)
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
column_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
                'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']

df = pd.read_csv(url, header=None, names=column_names)

# For demo purposes, we simulate categorical features (gender, family_history, activity)
# In your real dataset, replace these with actual columns
df['Gender'] = np.where(df['Pregnancies'] % 2 == 0, 'Male', 'Female')
df['FamilyHistory'] = np.where(df['DiabetesPedigreeFunction'] > 0.5, 'Yes', 'No')
df['Activity'] = np.where(df['Age'] > 30, 'Yes', 'No')

# Features and target
X = df[['Age', 'Gender', 'FamilyHistory', 'BloodPressure', 'Activity', 'BMI', 'Glucose']]
y = df['Outcome']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define preprocessing
numeric_features = ['Age', 'BMI', 'Glucose']
categorical_features = ['Gender', 'FamilyHistory', 'Activity']

numeric_transformer = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer([
    ('num', numeric_transformer, numeric_features),
    ('cat', categorical_transformer, categorical_features)
])

# Build pipeline
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
])

# Train pipeline
pipeline.fit(X_train, y_train)

# Evaluate
y_pred = pipeline.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("ROC AUC:", roc_auc_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Save pipeline
joblib.dump(pipeline, "DiabetesPipeline.joblib")
print("Pipeline saved as DiabetesPipeline.joblib")
