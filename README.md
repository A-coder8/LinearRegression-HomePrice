# 🏠 House Price Prediction

A beginner-friendly machine learning project for predicting house prices using **Multiple Linear Regression**.

The model uses several house features such as area, number of rooms, building age, floor, parking, elevator, warehouse, and location score to predict the price.

## 🚀 Features

* Multiple Linear Regression
* Multiple input features
* CSV dataset
* Train/Test split
* R² score evaluation
* Data visualization with Matplotlib
* House price prediction based on multiple features

## 🧠 Input Features

The model uses these features:

| Feature          | Description            |
| ---------------- | ---------------------- |
| `area`           | House area             |
| `room`           | Number of rooms        |
| `age`            | Building age           |
| `floor`          | Floor number           |
| `parking`        | Parking availability   |
| `elevator`       | Elevator availability  |
| `warehouse`      | Warehouse availability |
| `location_score` | Location score         |

### 🎯 Target

`price` — Predicted house price.

## 🛠️ Technologies

* Python
* NumPy
* Pandas
* Matplotlib
* Scikit-learn

## 📊 Model Evaluation

The model is evaluated using the **R² (R-squared) score**.

The project also includes a visualization comparing the house data with the model's predicted price.

## 📈 Visualization

The red line represents the predicted relationship between **house area** and **price**, while the blue points represent the dataset.

## 📁 Project Structure

```text
House-Price-Prediction/
│
├── house_price.csv
├── main.py
└── README.md
```

## ▶️ How to Run

Install the required libraries:

```bash
pip install numpy pandas matplotlib scikit-learn
```

Then run the Python file:

```bash
python main.py
```

## ⚠️ Note

The dataset used in this project is **synthetic data created for machine learning practice** and does not represent real-world housing prices.

## 🎯 Goal

The goal of this project is to practice:

* Data handling with Pandas
* Multiple Linear Regression
* Train/Test splitting
* Model evaluation
* Data visualization
* Making predictions with machine learning

---

Made for learning and practicing Machine Learning with Python. 🚀
