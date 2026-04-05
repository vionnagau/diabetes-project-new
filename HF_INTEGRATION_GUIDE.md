# 🤗 Hugging Face Hub Integration Guide

## Overview

This project is integrated with Hugging Face Hub for model storage, sharing, and versioning. Your trained Diabetes Risk model is pushed to the Hub so it can be easily shared, downloaded, and used by others.

---

## 📋 Quick Start (Choose One Method)

### Method 1: Automatic with GitHub Actions ⭐ (Recommended)

**Setup (One-time only):**

1. **Get your Hugging Face token:**
   - Go to https://huggingface.co/settings/tokens
   - Click **"New token"**
   - Name: `Write Token` (for pushing models)
   - Role: **Write**
   - Copy the token

2. **Add token to GitHub:**
   - Go to your GitHub repo → **Settings** → **Secrets and variables** → **Actions**
   - Click **"New repository secret"**
   - Name: `HF_TOKEN`
   - Value: Paste your Hugging Face token
   - Click **"Add secret"**

3. **Update the workflow file:**
   - Open `.github/workflows/push-model-to-hub.yml`
   - Replace `yourusername` with your actual Hugging Face username
   - Save and commit

**Usage:**
```bash
# Workflow automatically runs when you push model changes
git add DiabetesPipeline.joblib train_model.py
git commit -m "Update trained model"
git push origin main

# OR manually trigger in GitHub Actions tab → "Push Model to Hugging Face Hub" → "Run workflow"
```

**Advantage:** Fully automated, professional CI/CD pipeline

---

### Method 2: Manual Script (Quick & Easy)

**Setup:**

1. **Install hub package:**
   ```bash
   pip install huggingface-hub
   ```

2. **Get your token:**
   - Go to https://huggingface.co/settings/tokens
   - Create a **Write token**

3. **Export token:**
   ```bash
   export HF_TOKEN="your_token_here"
   # Or on Windows:
   set HF_TOKEN=your_token_here
   ```

4. **Update script:**
   - Open `push_to_hub.py`
   - Change `HF_REPO_ID = "your-username/diabetes-risk-model"` 
   - Replace `your-username` with your Hugging Face username

**Usage:**
```bash
python push_to_hub.py
```

**Output:**
```
✅ All files uploaded successfully!
🔗 View your model: https://huggingface.co/your-username/diabetes-risk-model
```

---

### Method 3: Direct CLI (Simple)

```bash
# Install
pip install huggingface-hub

# Login (one-time)
huggingface-cli login
# Paste your write token when prompted

# Push model
huggingface-cli upload your-username/diabetes-risk-model \
  DiabetesPipeline.joblib DiabetesPipeline.joblib

# Push model card
huggingface-cli upload your-username/diabetes-risk-model \
  HF_MODEL_CARD.md README.md
```

---

## 📁 YAML File Explanation

### `.github/workflows/push-model-to-hub.yml`

This file contains the **GitHub Actions workflow** - it's a CI/CD pipeline that automatically pushes your model to Hugging Face.

**What it does:**
```yaml
name: Push Model to Hugging Face Hub        # Workflow name

on:
  push:                                      # Trigger on:
    branches: [main]                         #   - Push to main branch
    paths: ['DiabetesPipeline.joblib', ...]  #   - When model files change
  workflow_dispatch:                         #   - Manual trigger button

jobs:
  push-model:                                # Job name
    runs-on: ubuntu-latest                  # Run on Ubuntu
    
    steps:
      - name: Checkout Repository           # Get code from GitHub
      - name: Set up Python 3.11            # Install Python
      - name: Install Dependencies          # pip install -r requirements.txt
      - name: Push Model to Hub             # Run upload script
        env:
          HF_TOKEN: ${{ secrets.HF_TOKEN }} # Use secret stored in GitHub
```

**Key Features:**
- ✅ Automatic on model updates
- ✅ Secure token storage (GitHub Secrets)
- ✅ Runs in isolated Ubuntu environment
- ✅ Error handling and logging

---

## 🎯 What Gets Uploaded

After running any method above, your Hugging Face Hub repo will contain:

```
your-username/diabetes-risk-model/
├── DiabetesPipeline.joblib        # Your trained model
├── README.md                        # Model documentation (HF_MODEL_CARD.md)
├── requirements.txt                 # Dependencies
├── train_model.py                  # Training code
└── .gitattributes                  # LFS configuration
```

---

## 🔍 Verify Upload Success

### Check on Hugging Face Hub

1. Go to https://huggingface.co/your-username/diabetes-risk-model
2. You should see:
   - ✓ Model card with documentation
   - ✓ Files listed (DiabetesPipeline.joblib, etc.)
   - ✓ Download button
   - ✓ Model usage examples

### Use in Python

```python
from huggingface_hub import hf_hub_download
import joblib

# Download model from Hub
model_path = hf_hub_download(
    repo_id="your-username/diabetes-risk-model",
    filename="DiabetesPipeline.joblib"
)

# Load and use
model = joblib.load(model_path)
predictions = model.predict(X_test)
```

---

## 🆘 Troubleshooting

| Problem | Solution |
|---------|----------|
| `HF_TOKEN not found` | Check `export HF_TOKEN="..."` or GitHub Secret |
| `Unauthorized (401)` | Token expired or read-only; get a new **Write** token |
| `Model file not found` | Ensure `DiabetesPipeline.joblib` exists in repo root |
| `Workflow not triggering` | Check `.github/workflows/push-model-to-hub.yml` path |
| `Repo not found` | Update `your-username` to your actual HF username |

**Debug command:**
```bash
huggingface-cli login --token $HF_TOKEN
huggingface-cli whoami  # Check if authenticated
```

---

## 💡 Pro Tips for Recruiters

✅ **GitHub Actions** shows you understand:
- CI/CD pipelines
- Automated workflows
- Secure credential management
- DevOps best practices

✅ **Hugging Face Hub** demonstrates:
- Model versioning & storage
- Reproducibility
- Collaboration in ML
- Production-ready thinking

✅ **Model Card** shows:
- Documentation skills
- Ethical AI awareness
- Professional standards

---

## 📚 Additional Resources

- **Hugging Face Hub Docs:** https://huggingface.co/docs/hub/
- **huggingface_hub Library:** https://github.com/huggingface/huggingface_hub
- **GitHub Actions Docs:** https://docs.github.com/en/actions

---

## 🚀 Next Steps

1. ✅ Create HF_TOKEN
2. ✅ Choose upload method (GitHub Actions or script)
3. ✅ Push your first model
4. ✅ Share repo URL with recruiters/team
5. ✅ Monitor downloads and engagement

---

**Questions?** Check official docs or open a GitHub issue!
