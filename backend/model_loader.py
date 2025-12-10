import pickle
import os

# Automatically find the model inside the backend folder
MODEL_PATH = os.path.join(os.path.dirname(__file__), "logistic_regression_model.pkl")

with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)

print("Model loaded successfully from:", MODEL_PATH)

