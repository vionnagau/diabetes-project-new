import os
from dotenv import load_dotenv
from huggingface_hub import HfApi

# Load environment variables from .env
load_dotenv()
token = os.getenv("HF_TOKEN")

api = HfApi()
api.upload_file(
    path_or_fileobj="Diabetesmodel.pkl",
    path_in_repo="Diabetesmodel.pkl",
    repo_id="vionnagau/diabetes-model",
    repo_type="model",
    token=token
)

print("Model uploaded successfully!")
