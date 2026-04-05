#!/usr/bin/env python3
"""
Push Diabetes Risk Model to Hugging Face Hub
Usage: python push_to_hub.py
"""

import os
from huggingface_hub import HfApi, login
from pathlib import Path

# Configuration
HF_REPO_ID = "your-username/diabetes-risk-model"  # Change this!
MODEL_FILE = "DiabetesPipeline.joblib"
MODEL_CARD_FILE = "HF_MODEL_CARD.md"

def push_model_to_hub():
    """Push trained model and model card to Hugging Face Hub"""
    
    # Get token from environment or prompt user
    token = os.getenv("HF_TOKEN")
    if not token:
        print("⚠️  HF_TOKEN not found in environment variables")
        print("Enter your Hugging Face write token:")
        token = input().strip()
    
    # Create API client
    api = HfApi()
    
    try:
        # Step 1: Create repo if it doesn't exist
        print(f"📝 Creating model repo: {HF_REPO_ID}...")
        api.create_repo(
            repo_id=HF_REPO_ID,
            repo_type="model",
            token=token,
            private=False,  # Set to True if you want private repo
            exist_ok=True
        )
        print("✓ Repository ready")
        
        # Step 2: Upload trained model
        print(f"\n📤 Uploading model file: {MODEL_FILE}...")
        api.upload_file(
            path_or_fileobj=MODEL_FILE,
            path_in_repo=MODEL_FILE,
            repo_id=HF_REPO_ID,
            repo_type="model",
            token=token,
            commit_message=f"Upload {MODEL_FILE}"
        )
        print(f"✓ Model uploaded successfully")
        
        # Step 3: Upload model card (README.md format)
        if Path(MODEL_CARD_FILE).exists():
            print(f"\n📤 Uploading model card: {MODEL_CARD_FILE}...")
            api.upload_file(
                path_or_fileobj=MODEL_CARD_FILE,
                path_in_repo="README.md",  # HF Hub expects README.md for model card
                repo_id=HF_REPO_ID,
                repo_type="model",
                token=token,
                commit_message="Upload model card documentation"
            )
            print(f"✓ Model card uploaded successfully")
        
        # Step 4: Upload additional files
        additional_files = [
            ("requirements.txt", "requirements.txt"),
            ("train_model.py", "train_model.py"),
        ]
        
        for local_file, repo_file in additional_files:
            if Path(local_file).exists():
                print(f"\n📤 Uploading {local_file}...")
                api.upload_file(
                    path_or_fileobj=local_file,
                    path_in_repo=repo_file,
                    repo_id=HF_REPO_ID,
                    repo_type="model",
                    token=token,
                    commit_message=f"Upload {local_file}"
                )
                print(f"✓ {local_file} uploaded successfully")
        
        # Success message
        print("\n" + "="*60)
        print("✅ All files uploaded successfully!")
        print("="*60)
        print(f"\n🔗 View your model: https://huggingface.co/{HF_REPO_ID}")
        print("\nYou can now:")
        print("  • Download the model from Hugging Face Hub")
        print("  • Share the model with others")
        print("  • Use it in other projects")
        print("  • Monitor model views and downloads")
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("\nTroubleshooting:")
        print("  1. Verify HF_TOKEN is correct (from huggingface.co/settings/tokens)")
        print("  2. Ensure you have write permissions")
        print("  3. Check that model files exist in current directory")
        return False
    
    return True

if __name__ == "__main__":
    print("🤗 Hugging Face Model Hub Uploader\n")
    
    # Check requirements
    try:
        from huggingface_hub import HfApi
    except ImportError:
        print("❌ huggingface-hub package not found")
        print("Install it with: pip install huggingface-hub")
        exit(1)
    
    # Change this to your actual username!
    if "your-username" in HF_REPO_ID:
        print("⚠️  Please update HF_REPO_ID at the top of this script!")
        print(f"   Current: {HF_REPO_ID}")
        print("   Change 'your-username' to your actual Hugging Face username")
        exit(1)
    
    # Run upload
    success = push_model_to_hub()
    exit(0 if success else 1)
