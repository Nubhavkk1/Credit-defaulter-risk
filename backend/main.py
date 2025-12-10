from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
from model_loader import model

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input model for single customer
class InputData(BaseModel):
    utilisation: float
    avg_payment_ratio: float
    min_due_paid_freq: float
    merchant_mix: float
    cash_withdrawal: float
    recent_spend_change: float

# -------------------------------
#      SINGLE CUSTOMER PREDICT
# -------------------------------
@app.post("/predict")
def predict(data: InputData):

    X = pd.DataFrame([{
        "Utilisation %": data.utilisation,
        "Avg Payment Ratio": data.avg_payment_ratio,
        "Min Due Paid Frequency": data.min_due_paid_freq,
        "Merchant Mix Index": data.merchant_mix,
        "Cash Withdrawal %": data.cash_withdrawal,
        "Recent Spend Change %": data.recent_spend_change
    }])

    probability = model.predict_proba(X)[0][1]

    return {"default_probability": float(probability)}


# -------------------------------
#          CSV PREDICTION
# -------------------------------
@app.post("/predict_csv")
async def predict_csv(file: UploadFile = File(...)):

    # Load CSV into DataFrame
    df = pd.read_csv(file.file)

    required_cols = [
        "Utilisation %",
        "Avg Payment Ratio",
        "Min Due Paid Frequency",
        "Merchant Mix Index",
        "Cash Withdrawal %",
        "Recent Spend Change %"
    ]

    # Ensure correct columns
    df = df[required_cols]

    # Predict probabilities
    probabilities = model.predict_proba(df)[:, 1].tolist()

    return probabilities
