import mlflow
import mlflow.sklearn
import pickle
from pathlib import Path

TRACKING_SERVER_HOST = "127.0.0.1"
TRACKING_SERVER_PORT = 5000

registry_uri = f"http://{TRACKING_SERVER_HOST}:{TRACKING_SERVER_PORT}"
tracking_uri = f"http://{TRACKING_SERVER_HOST}:{TRACKING_SERVER_PORT}"

mlflow.set_tracking_uri(tracking_uri)
mlflow.set_registry_uri(registry_uri)

RUN_NAME = "87b59ccf4e1543649b222948b792c4af"

loaded_model = mlflow.sklearn.load_model(f"runs:/{RUN_NAME}/model")

model_path = Path(__file__).resolve().parent / "model.pkl"

with open(model_path, "wb") as f:
    pickle.dump(loaded_model, f)



