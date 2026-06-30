# 🏠 Real Estate Price Prediction using Machine Learning

An end-to-end Machine Learning web application that predicts residential property prices in Bengaluru based on user inputs such as location, total square feet, number of bedrooms (BHK), and bathrooms. The project includes data preprocessing, feature engineering, model selection, interactive visualizations, and deployment using Streamlit.

---

## 📌 Project Overview

This project aims to estimate house prices in Bengaluru using historical housing data and machine learning techniques. The dataset undergoes extensive preprocessing, feature engineering, and outlier removal before training multiple regression models. The best-performing model is deployed through an interactive Streamlit web application that provides real-time predictions and data visualizations.

---

## ✨ Features

* 🏠 Predict house prices instantly
* 📍 Select property location from available locations
* 📐 Input total area, BHK, and bathrooms
* 🎨 Responsive Streamlit dashboard
* ⚡ Fast real-time predictions using a trained ML model

---

## 📂 Dataset

**Dataset:** Bengaluru House Price Dataset

The dataset contains residential property information including:

* Location
* Total Square Feet
* Number of Bedrooms (BHK)
* Bathrooms
* Price
* Area Type
* Society
* Availability
* Balcony

---

## 🧹 Data Preprocessing

The following preprocessing steps were performed:

* Removed unnecessary columns
* Handled missing values
* Converted BHK from the Size column
* Converted Total Square Feet into numerical values
* Created Price per Square Foot feature
* Reduced high-cardinality locations by grouping rare locations into "Other"
* Removed outliers using business logic
* Removed BHK and bathroom inconsistencies
* One-Hot Encoding of categorical variables

---

## 🤖 Machine Learning Models

The following regression models were trained and evaluated:

* Linear Regression
* Lasso Regression
* Decision Tree Regressor

Hyperparameter tuning was performed using **GridSearchCV**, and model validation was done using **ShuffleSplit Cross Validation**.

The best-performing model was selected and saved using Pickle.

---

## 📊 Model Performance

The deployed application displays model evaluation metrics such as:

* R² Score
* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)

---

## 🛠️ Tech Stack

| Category             | Technology    |
| -------------------- | ------------- |
| Programming Language | Python        |
| Machine Learning     | Scikit-learn  |
| Data Processing      | Pandas, NumPy |
| Visualization        | Plotly        |
| Web Framework        | Streamlit     |
| Model Serialization  | Pickle        |
| Version Control      | Git & GitHub  |

---

## 📁 Project Structure

```text
Real-Estate-Price-Prediction/
│
├── app.py
├── util.py
├── README.md
│
├── artifacts/
│   ├── model.pkl
│   ├── columns.json
│   ├── house_data.csv
│   └── model_metrics.json
│
├── dataset/
│   └── Bengaluru_House_Data.csv
│
├── notebook/
    └── Real_Estate_Price_Prediction.ipynb

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/gkrnitr2027/Real-Estate-Price-Prediction.git
```

### Navigate to the project folder

```bash
cd Real-Estate-Price-Prediction
```

### Run the application

```bash
streamlit run app.py
