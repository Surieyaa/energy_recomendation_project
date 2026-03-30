# ⚡ Energy Consumption Prediction using Machine Learning

## 📌 Project Overview
This project aims to predict electricity consumption using Machine Learning techniques based on historical and environmental data. The system analyzes patterns in energy usage and provides accurate predictions to help optimize energy consumption and reduce wastage.

---

## 🚀 Features
- 🔮 Predict energy consumption
- 📈 Identify peak usage patterns
- 💡 Provide energy-saving suggestions
- 🌐 Interactive web app using Streamlit
- 📊 Data visualization (heatmap, feature importance)

---

## 🧠 Technologies Used
- Python  
- Pandas, NumPy  
- Scikit-learn  
- XGBoost  
- Matplotlib, Seaborn  
- Streamlit  
- Joblib  

---

## 📊 Dataset Description
The dataset contains time-series energy usage data with features such as:

- Temperature  
- Humidity  
- Timestamp  
- Voltage, Current (removed to avoid leakage)  
- Other system/environment parameters  

### 🎯 Target Variable:
- Energy / Power Consumption  

---

## ⚙️ Data Preprocessing
- Removed duplicate values  
- Handled missing data  
- Converted timestamp into:
  - Hour  
  - Day  
  - Month  
  - Weekday  
- Removed data leakage features  

---

## 🔥 Feature Engineering
To improve accuracy, the following features were added:

- ⏳ Lag Features:
  - Lag1, Lag2, Lag3  
- 📉 Rolling Statistics:
  - Rolling Mean  
  - Rolling Standard Deviation  
- 📅 Time-based Features  

These help capture temporal dependencies in energy usage.

---

## 🤖 Machine Learning Models
Two models were used:

### 🌳 Random Forest Regressor
- Handles non-linear data
- Reduces overfitting

### ⚡ XGBoost Regressor
- High performance boosting algorithm
- Better accuracy and efficiency

---

## 📈 Model Evaluation
Models were evaluated using:

- R² Score (Accuracy)
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

### ✅ Final Accuracy:
- Achieved approximately **85–90% accuracy**

---

## 🌐 Streamlit Web Application
The project is deployed as an interactive web app using Streamlit.

### 📥 User Inputs:
- Temperature  
- Humidity  
- Time (Hour, Day, Month, Weekday)  
- Previous energy usage (Lag values)  

### 📤 Output:
- Predicted energy consumption  
- Energy-saving suggestions  

---

## ▶️ How to Run the Project

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt