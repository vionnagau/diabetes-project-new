#!/usr/bin/env bash
set -euo pipefail

if [[ -z "${HF_TOKEN:-}" ]]; then
  echo "ERROR: HF_TOKEN environment variable is not set."
  echo "Set HF_TOKEN before running this script:"
  echo "  export HF_TOKEN=your_token_here"
  exit 1
fi

REPO_URL="https://x-access-token:${HF_TOKEN}@huggingface.co/spaces/vionnagau/diabetes-project-new.git"

if ! command -v git-lfs >/dev/null 2>&1; then
  echo "Installing Git LFS..."
  if command -v sudo >/dev/null 2>&1; then
    sudo apt-get update
    sudo apt-get install -y git-lfs
  else
    echo "ERROR: git-lfs is required but sudo is not available."
    exit 1
  fi
fi

git lfs install --local

# Ensure remote is configured correctly
if git remote get-url hf >/dev/null 2>&1; then
  git remote set-url hf "$REPO_URL"
else
  git remote add hf "$REPO_URL"
fi

# Push the current branch to HF Spaces main branch
CURRENT_BRANCH=$(git branch --show-current)
echo "Pushing branch '$CURRENT_BRANCH' to Hugging Face Spaces main branch..."

git push --force hf "$CURRENT_BRANCH:main"

echo "✔ Code pushed successfully."

if ! python3 -c "import huggingface_hub" >/dev/null 2>&1; then
  python3 -m pip install --upgrade pip
  python3 -m pip install huggingface-hub hf-xet
fi

echo "Uploading DiabetesPipeline.joblib via Hugging Face API..."
python3 - <<'PY'
import os
from huggingface_hub import HfApi

repo_id = "vionnagau/diabetes-project-new"
token = os.environ["HF_TOKEN"]
api = HfApi()
api.upload_file(
    path_or_fileobj="DiabetesPipeline.joblib",
    path_in_repo="DiabetesPipeline.joblib",
    repo_id=repo_id,
    repo_type="space",
    token=token
)
print("✔ DiabetesPipeline.joblib uploaded successfully.")
PY
