Problem & Solution
Problem

Banks face financial losses when customers default on credit card payments.
The dataset available for this project originally contained only 100 rows, which was too small to train a stable ML model.

Solution

To improve model performance, additional data rows were created by following the natural patterns of the original dataset and introducing slight valid randomization.
This expanded dataset was then used to train a Logistic Regression model that predicts the probability of next-month default.

The model is deployed through:

 A FastAPI backend for serving predictions

 A lightweight HTML/CSS/JS frontend

 CSV upload support for batch predictions(must be in the same format )

Each prediction returns both a default probability and an automatic risk label:
🟢 Low · 🟡 Medium · 🔴 High

📦 Project Structure
credit_defaulter_prediction/
│
├── backend/
│   ├── main.py                       # FastAPI server + routes
│   ├── model_loader.py               # Loads saved ML model
│   ├── logistic_regression_model.pkl # Trained ML model
│   ├── requirements.txt              # Backend dependencies
│
└── frontend/
    ├── index.html                    # User Interface
    ├── styles.css                    # UI Styling
    ├── script.js                     # API Integration + Logic



            Features


✔ Single Customer Prediction

Enter:

Utilisation %

Avg Payment Ratio

Min Due Paid Frequency

Merchant Mix Index

Cash Withdrawal %

Recent Spend Change %

Output:

Default probability

Risk label (Low / Medium / High)


✔ CSV Batch Prediction

Upload a CSV containing the same feature columns to receive:

Predictions for each row

Risk categorization

Table view of results.


📊 Machine Learning Model

Algorithm: Logistic Regression

Framework: scikit-learn

Trained on original + synthetically expanded dataset

Predicts next-month credit card default probability

👤 Author

Anubhav
Credit Defaulter Prediction — Submission Branch

🔗 Submission Link:
https://github.com/Nubhavkk1/Credit-defaulter-risk/tree/submission