---
title: Diabetes Project
emoji: 🩺
colorFrom: blue
colorTo: green
sdk: streamlit
sdk_version: "1.32.0"
python_version: "3.10"
app_file: diabetes_app.py
pinned: false
---

# 🩺 Diabetes Risk Assessment System

A production-ready diabetes risk assessment platform that combines machine learning, REST APIs, interactive dashboards, and cloud deployment. This repository presents a complete ML engineering workflow from data ingestion and preprocessing to model serving and public deployment.

---

## 🚀 Live Demo

**Open the live application now — no installation required.**

### [→ Launch the Streamlit Dashboard](https://huggingface.co/spaces/vionnagau/diabetes-project-new)

A browser-based interface for entering health metrics and receiving an immediate diabetes risk prediction from a trained scikit-learn model.

---

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| **Language** | Python 3.12 |
| **ML & Data** | scikit-learn, pandas, NumPy, joblib |
| **API** | FastAPI, Uvicorn |
| **UI** | Streamlit, Tkinter |
| **Deployment** | Docker, GitHub Actions, Hugging Face Spaces |
| **DevOps** | Git, Git LFS |

---

## 🧩 Project Overview

This project includes:

- **Model training pipeline** with feature engineering and a Random Forest classifier
- **API service** that loads a serialized model and exposes prediction endpoints
- **Streamlit dashboard** for end-user interaction and visual feedback
- **Tkinter desktop prototype** for local application testing
- **Deployment automation** via scripts and GitHub Actions

---

## 📁 Repository Layout

```text
diabetes-project-new/
├── app/
│   └── api.py                   # FastAPI endpoints and model inference
├── tests/                       # Validation and regression tests
├── .github/
│   └── workflows/
│       └── sync.yml             # Hugging Face sync workflow
├── Dockerfile                   # Container build instructions
├── app.py                       # Streamlit web application
├── dashboard.py                 # Alternative dashboard interface
├── diabetes_app.py              # Tkinter desktop UI
├── train_model.py               # ML pipeline and training script
├── DiabetesPipeline.joblib      # Serialized trained model
├── requirements.txt             # Python dependencies
├── sync_to_hf.sh                # HF Spaces sync helper
└── README.md                    # Project documentation
```

---

## ✨ Core Features

- **ML pipeline** with data imputation, scaling, categorical encoding, and model fitting
- **FastAPI backend** for low-latency prediction requests
- **Streamlit frontend** for clean, interactive user input and result display
- **Container-ready** architecture for reliable deployment
- **Cloud deployment** via Hugging Face Spaces with automated sync support

---

## 🔧 Technical Highlights

- **Data preprocessing** using `ColumnTransformer`, `SimpleImputer`, `StandardScaler`, and `OneHotEncoder`
- **Model persistence** with `joblib` for fast inference loading
- **Asynchronous API design** using FastAPI and Uvicorn
- **Responsive dashboard** built with Streamlit caching for performance
- **Reproducibility** with dependency pinning and environment isolation
- **Deployment automation** using shell scripts and GitHub Actions workflows

---

## 📦 Installation

**Clone the repository:**

```bash
git clone https://github.com/vionnagau/diabetes-project-new.git
cd diabetes-project-new
```

**Create an isolated environment:**

```bash
python3 -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**Verify the environment:**

```bash
python3 -c "import joblib; print('✓ Environment ready')"
```

---

## ▶️ Quick Start

**Run the Streamlit dashboard**

```bash
streamlit run app.py
```

**Start the FastAPI backend**

```bash
uvicorn app.api:app --reload --port 8000
```

**Launch the desktop UI**

```bash
python3 diabetes_app.py
```

**Run the test suite**

```bash
pytest tests/ -v
```

---

## ☁️ Deployment

### Local deployment
Use the Quick Start commands above for local testing and development.

### Hugging Face Spaces
This project is configured for public deployment on Hugging Face Spaces. The repository includes the required app configuration and sync workflow.

**Deployment helper:**

```bash
export HF_TOKEN="your_hf_write_token"
bash sync_to_hf.sh
```

> ⚠️ **Important:** Do not commit secret tokens. Use environment variables only.

---

## 📌 Notes

- The Streamlit app is the primary user interface and is optimized for fast inference.
- The FastAPI backend can be used for integration with other applications or services.
- The model is serialized as `DiabetesPipeline.joblib` and loaded at runtime.

---

## 📧 Contact

Open an issue or reach out if you have questions about the implementation, architecture, or deployment.

---

**Built with Python, scikit-learn, and modern ML deployment practices.**
