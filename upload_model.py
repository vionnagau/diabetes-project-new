from huggingface_hub import HfApi

api = HfApi()
api.upload_file(
    path_or_fileobj="Diabetesmodel.pkl",
    path_in_repo="Diabetesmodel.pkl",
    repo_id="vionnagau/diabetes-model",
    repo_type="model"
)

print("Model uploaded successfully!")
