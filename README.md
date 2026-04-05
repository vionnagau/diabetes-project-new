# Diabetes Risk Assessment System

A complete diabetes risk assessment project built to demonstrate practical skills in machine learning, API development, interactive visualization, deployment, and automation. This repository is designed for recruiters reviewing internship candidates in cloud services, product operations, data analytics, or AI engineering.

## Overview

This project includes a full end-to-end workflow:
- data processing and model training with `scikit-learn`
- REST API deployment using `FastAPI`
- interactive web dashboard using `Streamlit`
- desktop prototype using `Tkinter`
- containerization with `Docker`
- sync and automation support for Hugging Face Spaces integration

The repository is designed to be clean, professional, and easy to run locally.

## Technology Stack

| Category | Technologies |
|---|---|
| Programming Languages | Python 3.11+, Shell/Bash |
| ML & Data | scikit-learn, pandas, NumPy, joblib |
| Backend | FastAPI, Uvicorn |
| Frontend / UI | Streamlit, Tkinter |
| Deployment | Docker, GitHub Actions, Hugging Face Spaces |
| Versioning/Automation | Git, GitHub Actions, Git LFS, shell scripts |
| Documentation | Markdown, model card, integration guide |

## Repo Structure

```
diabetes-project-new/
├── .github/
│   └── workflows/
│       └── sync.yml                 # Hugging Face sync workflow
├── .gitattributes                   # LFS configuration
├── .gitignore                       # ignored files
├── Dockerfile                       # container setup for API
├── HF_INTEGRATION_GUIDE.md          # Hugging Face deployment guide
├── HF_MODEL_CARD.md                 # model card documentation
├── README.md                        # this file
├── app/api.py                       # FastAPI endpoint implementation
├── dashboard.py                     # Streamlit dashboard app
├── diabetes_app.py                  # Tkinter desktop application
├── train_model.py                   # model training pipeline
├── DiabetesPipeline.joblib          # trained serialized model
├── Diabetesmodel.pkl                # alternative model file
├── push_to_hub.py                   # Hugging Face upload helper script
├── requirements.txt                 # Python dependencies
├── sync_to_hf.sh                    # local sync helper script
└── tests/                           # test and validation code
```

## Key Features

- **Machine Learning Pipeline**: Builds and saves a predictive model for diabetes risk using data preprocessing and a Random Forest classifier.
- **REST API**: Provides prediction endpoints through FastAPI for integration with other applications.
- **Interactive Dashboard**: Streamlit interface for user input, visualization, and immediate prediction feedback.
- **Desktop UI Prototype**: Tkinter-based application for local user interaction.
- **Deployment Ready**: Dockerfile and automation scripts support reproducible deployment.
- **Hugging Face Sync**: Workflow and scripts manage synchronization with Hugging Face Spaces without exposing secrets.

## Why This Project Is Relevant

This project is designed to highlight skills that are directly valuable for internship roles in cloud services, product operations, and data-driven teams:

- **Cloud-ready delivery**: containerization and sync workflows demonstrate deployment maturity.
- **Data and analytics orientation**: model training and dashboard work show practical data experience.
- **Automation mindset**: GitHub Actions and shell scripts highlight process automation skills.
- **Product-aware engineering**: multiple interfaces (API, dashboard, desktop app) show user-focused implementation.

## Installation

Use the GitHub clone URL below to get the repository locally. This is the correct URL for the repository and is safe for recruiters and collaborators:

```bash
git clone https://github.com/vionnagau/diabetes-project-new.git
cd diabetes-project-new
```

Create a Python virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

> Note: The `README` URL uses `diabetes-project-new`, which matches the actual GitHub repository name. The `.git` suffix is standard for clone URLs and is correct.

## Local Usage

### Run the Streamlit dashboard

```bash
streamlit run dashboard.py
```

### Run the FastAPI backend

```bash
uvicorn app.api:app --reload --port 8000
```

### Run the desktop UI

```bash
python diabetes_app.py
```

### Run tests

```bash
pytest tests/ -v
```

## Deployment and Sync

Recruiters do not need any token or secret to run the project locally. The following deployment commands are only required for project maintenance and Hugging Face sync by the repository owner.

### Hugging Face sync (optional, maintainer only)

This project includes a helper script and workflow to sync the repository with Hugging Face Spaces. If you maintain the project, use an environment variable for the token:

```bash
export HF_TOKEN="your_hf_write_token"
bash sync_to_hf.sh
```

> This token command is optional and only for deployment automation. It is not required for running the app locally.

## Notes for Recruiters

- No secret or token is required for cloning or running the project.
- The main local commands are `streamlit run dashboard.py`, `uvicorn app.api:app --reload --port 8000`, and `python diabetes_app.py`.
- This repository is intentionally structured to be easy to understand, maintain, and extend.

## Contact

If you want to discuss this project or the skills demonstrated, I am happy to explain the technical architecture, data decisions, and deployment choices.
