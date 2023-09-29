import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel


class Features(BaseModel):
    X: list


app = FastAPI()

model_file_path = "model/regression_lineaire.joblib"
model = joblib.load(model_file_path)


@app.post("/predict")
async def predict(features: Features):
    X = np.array(features.X)

    return {"prediction": model.predict(X).tolist()}
