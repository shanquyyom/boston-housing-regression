# 🏠 Boston Housing Price Prediction – ML Regression Project

Welcome to the **Boston Housing ML API Project**, a complete end-to-end regression analysis and deployment pipeline. This project predicts house prices in Boston based on multiple features using various machine learning models, evaluation metrics, and deployment using FastAPI.

---

## 📌 Project Highlights

- 📊 Applied **Multiple Regression Algorithms**
- ✅ Used **K-Fold Cross Validation**
- 🔍 Performed **Hyperparameter Tuning** (GridSearchCV, RandomizedSearchCV)
- 🏆 Selected the **Best Model**
- 🚀 Deployed using **FastAPI**
- 📁 Modular Project Structure

---

## 📂 Project Structure

boston-housing-ml-api/
│
├── boston_api/ # FastAPI app with model deployment
│ ├── main.py # Main FastAPI application
│ ├── model.pkl # Saved ML model (best regressor)
│ └── requirements.txt # Python dependencies
│
├── boston_regression_models.ipynb # Notebook with EDA, ML models, evaluation
├── README.md # You're reading it!


---

## 🧠 Machine Learning Models Used

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- K-Nearest Neighbors (KNN)
- Gradient Boosting Regressor
- AdaBoost Regressor
- Bagging Regressor
- Stacking Regressor
- Support Vector Regressor (SVR)

---

## 📈 Evaluation Metrics

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

Hyperparameter tuning applied via:
- ✅ `GridSearchCV`
- 🎲 `RandomizedSearchCV`

---

## 🚀 FastAPI Deployment

The selected model was saved using `joblib` and deployed using **FastAPI** with the following steps:

- `/predict` endpoint to send input and receive predicted house price.
- Input: JSON with all model features
- Output: Predicted price as float

### 🔧 To Run Locally:

```bash
cd boston_api
pip install -r requirements.txt
uvicorn main:app --reload
Then open: http://127.0.0.1:8000/docs to test with Swagger UI

📌 Dataset Info
Dataset: Boston Housing (from sklearn)

Features: CRIM, ZN, INDUS, NOX, RM, AGE, etc.

Target: MEDV (Median house value)

🧑‍💻 Author
Shan Quyyoom
📍 Jhang, Pakistan
📧 shanquyyoom99@gmail.com
🔗 https://www.linkedin.com/in/shan-quyyoom-452923365
