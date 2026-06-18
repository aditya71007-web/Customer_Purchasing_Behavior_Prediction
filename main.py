from fastapi import FastAPI
from schema import CustomerData, PredictionResponse
from model import predict_behavior, get_accuracy
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(
    title="Customer Purchasing Behavior Prediction API"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Development ke liye
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "Customer Purchasing Behavior Prediction API is Running"
    }


@app.get("/accuracy")
def accuracy():
    return {
        "accuracy": get_accuracy()
    }


@app.post("/predict",response_model=PredictionResponse)
def predict(data: CustomerData):
    result = predict_behavior(
        data.age,
        data.annual_income,
        data.previous_purchases
    )
    return result