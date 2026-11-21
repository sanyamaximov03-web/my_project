import pickle 
from pathlib import Path
import pandas as pd

MODEL_PATH = (Path(__file__).resolve().parent.parent
              / "models"
              / "model.pkl")

class FastAPIHandler:

    def  __init__(self):
        with open(MODEL_PATH, "rb") as file:
            self.model = pickle.load(file)

    def predict(self, item_features: dict):
        df = pd.DataFrame([item_features])
        prediction = self.model.predict(df)
        return float(prediction[0])