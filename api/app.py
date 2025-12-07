from fastapi import FastAPI
import pandas as pd
import joblib
import json
import os

app = FastAPI(title="FraudShield AI API")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "fraud_model.pkl")
COLUMNS_PATH = os.path.join(BASE_DIR, "models", "model_columns.json")

model = joblib.load(MODEL_PATH)

with open(COLUMNS_PATH, "r") as f:
    model_columns = json.load(f)


@app.get("/")
def home():
    return {"status": "FraudShield API is running"}


@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])

    df = pd.get_dummies(df)

    df = df.reindex(columns=model_columns, fill_value=0)

    prediction = int(model.predict(df)[0])
    probability = float(model.predict_proba(df)[0][1])

    result = "Fraud" if prediction == 1 else "Legitimate"

    return {
        "prediction": result,
        "fraud_probability": round(probability, 4)
    }
