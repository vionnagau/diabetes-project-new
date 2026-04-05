#!/usr/bin/env bash
set -euo pipefail

if [[ -z "${HF_TOKEN:-}" ]]; then
  echo "ERROR: HF_TOKEN environment variable is not set."
  echo "Set HF_TOKEN before running this script:"
  echo "  export HF_TOKEN=your_token_here"
  exit 1
fi

REPO_URL="https://x-access-token:${HF_TOKEN}@huggingface.co/spaces/vionnagau/diabetes-project-new.git"

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

echo "✔ Sync completed successfully."
