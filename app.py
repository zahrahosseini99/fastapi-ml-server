from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load model
model = joblib.load("model.joblib")

app = FastAPI()

class IrisInput(BaseModel):
    data: list  # Example: [5.1, 3.5, 1.4, 0.2]

@app.post("/predict")
def predict(input_data: IrisInput):
    features = np.array([input_data.data])
    prediction = int(model.predict(features)[0])
    return {"prediction": prediction}
