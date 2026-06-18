import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Dataset
data = np.array([[25, 50000, 2],[30, 60000, 1],[35, 70000, 0],[40, 80000, 2],[45, 90000, 3],[50, 100000, 2]])

labels = np.array([0, 0, 1, 1, 2, 2])

# Train-Test Split
x_train, x_test, y_train, y_test = train_test_split(
    data,
    labels,
    test_size=0.33,
    random_state=42
)

# Feature Scaling
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# Train Model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train, y_train)


def get_accuracy():
    return knn.score(x_test, y_test)


def predict_behavior(age, annual_income, previous_purchases):
    user_data = np.array(
        [[age, annual_income, previous_purchases]]
    )

    user_data = scaler.transform(user_data)

    prediction = knn.predict(user_data)[0]

    behavior = {
        0: "Low Purchasing",
        1: "Medium Purchasing",
        2: "High Purchasing"
    }

    return {
        "purchasing_behavior": behavior[prediction],
        "class_id": int(prediction)
    }