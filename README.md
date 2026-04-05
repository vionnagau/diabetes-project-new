---
title: Diabetes Risk Assessment System
emoji: "🩺"
colorFrom: blue
colorTo: green
sdk: streamlit
python_version: "3.12"
app_file: app.py
pinned: false
---

# 🩺 Diabetes Risk Assessment System

A production-ready diabetes risk assessment platform combining machine learning, REST APIs, interactive dashboards, and cloud deployment. This project showcases a complete ML engineering workflow from data pipeline to public deployment.

---

## 🚀 Live Demo

**Try it now** – No installation required:

### **[→ Launch Streamlit Dashboard](https://huggingface.co/spaces/vionnagau/diabetes-project-new)**

Input your health metrics and receive instant diabetes risk predictions powered by a trained scikit-learn Random Forest model.

---

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| **Languages** | Python 3.12, Shell/Bash |
| **ML & Data** | scikit-learn, pandas, NumPy, joblib |
| **Backend** | FastAPI, Uvicorn |
| **Frontend** | Streamlit, Tkinter |
| **Deployment** | Docker, GitHub Actions, Hugging Face Spaces |
| **DevOps** | Git, Git LFS, GitHub Actions |

---

## 📁 Project Structure

```
diabetes-project-new/
├── app/
│   └── api.py                   # FastAPI endpoints
├── tests/                       # Test suite
├── .github/
│   └── workflows/
│       └── sync.yml             # Hugging Face sync workflow
├── Dockerfile                   # Container configuration
├── app.py                       # Streamlit web app
├── dashboard.py                 # Dashboard interface
├── diabetes_app.py              # Desktop UI (Tkinter)
├── train_model.py               # ML pipeline & training
├── DiabetesPipeline.joblib      # Trained model
├── requirements.txt             # Dependencies
├── sync_to_hf.sh                # HF sync script
└── README.md                    # Documentation
```

---

## ✨ Features

- 🤖 **ML Pipeline**: Random Forest classifier with preprocessing (imputation, scaling, encoding)
- 🔌 **REST API**: FastAPI endpoints for programmatic predictions
- 📊 **Web Dashboard**: Interactive Streamlit interface with real-time predictions
- 🖥️ **Desktop App**: Tkinter-based local UI alternative
- 🐳 **Containerized**: Docker support for consistent deployment
- ☁️ **Cloud Ready**: Automated Hugging Face Spaces sync with GitHub Actions

---

## 💡 Technical Highlights

- **ML Engineering**: Data preprocessing, model training, and hyperparameter tuning with scikit-learn
- **Backend Development**: RESTful API design with FastAPI and async Python
- **Frontend**: Interactive UIs with Streamlit and Tkinter
- **DevOps**: Docker containerization, GitHub Actions CI/CD, Git LFS for large files
- **Cloud Deployment**: Automated sync to Hugging Face Spaces with secure token handling
- **Reproducibility**: Version pinning and environment isolation for consistent builds

---

## 📦 Installation

**Clone the repository:**

```bash
git clone https://github.com/vionnagau/diabetes-project-new.git
cd diabetes-project-new
```

**Set up environment:**

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**Verify setup:**

```bash
python3 -c "import joblib; print('✓ Environment ready')"
```

---

## 🎯 Quick Start

**Web Dashboard** (Recommended)
```bash
streamlit run app.py
# Opens at http://localhost:8501
```

**REST API**
```bash
uvicorn app.api:app --reload --port 8000
# API docs at http://localhost:8000/docs
```

**Desktop Application**
```bash
python3 diabetes_app.py
```

**Tests**
```bash
pytest tests/ -v
```

---

## 🚀 Deployment

### Local Deployment
No external setup required. Clone, install, and run with the Quick Start commands above.

### Cloud Deployment (Hugging Face Spaces)
The web app is automatically deployed to Hugging Face Spaces via GitHub Actions. Monitor syncs in the Actions tab.

**For maintainers:** Trigger manual sync with:
```bash
export HF_TOKEN="your_hf_write_token"
bash sync_to_hf.sh
```

> ⚠️ **Security Note:** Never commit tokens. Use environment variables only.

---

## 📧 Questions?

Open an issue or reach out with questions about the implementation, architecture, or deployment approach.

---

**Built with ❤️ using Python, scikit-learn, and modern ML engineering practices.**
