from pydantic import BaseModel


class CustomerData(BaseModel):
    age: int
    annual_income: float
    previous_purchases: int


class PredictionResponse(BaseModel):
    purchasing_behavior: str
    class_id: int