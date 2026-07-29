# 🚗 Car Price Prediction using Multiple Linear Regression

A Machine Learning project that predicts the price of used cars based on their specifications such as brand, model, fuel type, transmission, mileage, engine size, and other vehicle attributes.

---

## 🌐 Live Demo

🔗 Web App: https://car-price-prediction-z.streamlit.app/

---

## 📸 Project Preview

> *(Add screenshots of your Streamlit application here)*

---

## 📌 Project Overview

This project demonstrates a complete end-to-end Machine Learning workflow for predicting used car prices.

The project covers:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Data Preprocessing
- Feature Engineering
- Multiple Linear Regression
- Model Evaluation
- Model Deployment using Streamlit

---

## 💼 Business Problem

Estimating the market price of a used car is challenging because several factors influence its value.

This project helps estimate a fair selling price by analyzing historical vehicle data and applying Machine Learning.

---

## 🎯 Project Objectives

- Understand the dataset
- Analyze factors affecting car prices
- Build an accurate prediction model
- Evaluate model performance
- Deploy the trained model as a web application

---

# 📊 Dataset Information

| Feature | Details |
|----------|---------|
| Dataset | Used Cars Dataset |
| Rows | 71,593 |
| Columns | 10 |
| Missing Values | 0 |
| Duplicate Rows Removed | 842 |
| Target Variable | price |

---

# 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Streamlit
- Joblib
- Jupyter Notebook

---

# 📈 Exploratory Data Analysis

Performed analysis including:

- Univariate Analysis
- Bivariate Analysis
- Multivariate Analysis
- Correlation Analysis
- Distribution Analysis
- Outlier Detection

---

# ⚙️ Data Preprocessing

Steps performed:

- Duplicate Removal
- Feature & Target Separation
- One-Hot Encoding
- Feature Scaling
- Column Transformer
- Train-Test Split (80:20)
- Pipeline Implementation

---

# 🤖 Machine Learning Model

**Algorithm Used**

- Multiple Linear Regression

---

# 📊 Model Performance

| Metric | Score |
|---------|--------|
| R² Score | 0.8878 |
| MAE | 2073.39 |
| MSE | 9851820.63 |
| RMSE | *(Update manually)* |

---

# 🚀 Streamlit Application Features

- Interactive User Interface
- Dynamic Dropdown Menus
- Real-time Price Prediction
- Clean Dashboard Layout
- Machine Learning Pipeline Integration

---

# 📂 Project Structure

```text
Car-Price-Prediction/
│
├── app/
│   └── app.py
│
├── data/
│   └── raw/
│       └── cars_dataset.csv
│
├── images/
│
├── models/
│   └── used_car_price_predictor.pkl
│
├── notebook/
│   └── Car_Price_Prediction.ipynb
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🚀 Installation

```bash
git clone <repository-url>

cd Car-Price-Prediction

pip install -r requirements.txt
```

---

# ▶️ Run the Application

```bash
streamlit run app/app.py
```

---

# 👨‍💻 Author

**Sahil Rohilla**

💼 LinkedIn:
https://www.linkedin.com/in/sahil-rohilla-7436a635a/
💻 GitHub:
https://github.com/rohilasahil86-ai

🌐 Live App:
https://car-price-prediction-z.streamlit.app/

---

## ⭐ If you found this project useful, don't forget to give it a Star!