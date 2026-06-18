# Customer Purchasing Behavior Prediction using KNN and FastAPI

## Project Overview

This project predicts customer purchasing behavior using the K-Nearest Neighbors (KNN) Machine Learning algorithm. The application takes customer details such as age, annual income, and previous purchases as input and predicts whether the customer's purchasing behavior is Low, Medium, or High.

The project is built using:

* FastAPI for backend API development
* Scikit-learn for Machine Learning
* HTML, CSS, and JavaScript for the frontend interface

---

## Features

* Predict customer purchasing behavior in real time.
* REST API built with FastAPI.
* Interactive frontend using HTML, CSS, and JavaScript.
* Input validation using Pydantic schemas.
* Trained KNN model with feature scaling.

---

## Project Structure

project/
│
├── main.py
├── model.py
├── schema.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
└── style.css

---

## Technologies Used

* Python
* FastAPI
* Scikit-learn
* NumPy
* Pydantic
* HTML5
* CSS3
* JavaScript

---

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd customer-purchasing-prediction
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate Virtual Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux/Mac

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
python -m uvicorn main:app --reload
```

Server will start at:

http://127.0.0.1:8000

Frontend:

http://127.0.0.1:8000

API Documentation:

http://127.0.0.1:8000/docs

---

## API Endpoint

### Predict Purchasing Behavior

**Endpoint**

```
POST /predict
```

**Request Body**

```json
{
  "age": 28,
  "annual_income": 55000,
  "previous_purchases": 1
}
```

**Response**

```json
{
  "purchasing_behavior": "Low Purchasing",
  "class_id": 0
}
```

---

## Purchasing Behavior Classes

| Class ID | Behavior          |
| -------- | ----------------- |
| 0        | Low Purchasing    |
| 1        | Medium Purchasing |
| 2        | High Purchasing   |

---

## Machine Learning Workflow

1. Load customer dataset.
2. Split data into training and testing sets.
3. Apply feature scaling using StandardScaler.
4. Train the KNN classifier.
5. Accept user input from the frontend.
6. Predict purchasing behavior using the trained model.
7. Display prediction results on the web interface.

---

## Future Improvements

* Use a larger real-world customer dataset.
* Store prediction history in a database.
* Add charts and analytics dashboard.
* Deploy using Docker and cloud platforms.
* Improve model accuracy through hyperparameter tuning.

---

## Author

Aditya Kumar

