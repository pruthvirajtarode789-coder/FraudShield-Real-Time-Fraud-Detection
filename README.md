🛡️ FraudShield — Real-Time Fraud Detection System

🚨 Enterprise-Grade AI System for Real-Time Transaction Fraud Prevention

FraudShield is a Machine Learning powered fraud detection system designed to help banks, fintech firms, and digital payment platforms detect suspicious transactions instantly with high accuracy.

✅ Key Features

✅ Real-Time Fraud Prediction

✅ AI Risk Scoring Engine

✅ Production-Ready FastAPI

✅ Interactive Streamlit Dashboard

✅ Cloud Deployable

✅ Modular ML Pipeline

✅ Client-Ready Architecture

🧠 System Overview

FraudShield consists of three main components:

Module	Description
🏋️‍♂️ Training Module	Trains Logistic Regression model
🚀 FastAPI Server	Serves real-time predictions
🖥️ Streamlit App	Client dashboard & visualization
📁 Project Structure
FraudShield-Real-Time-Fraud-Detection/
│
├── api/              → FastAPI backend
├── app/              → Streamlit UI
├── training/         → ML Training Scripts
├── models/           → Saved Model Files
├── data/raw/         → Dataset
├── diagrams/         → All System Diagrams
├── requirements.txt
└── README.md

⚙️ Technology Stack

Python

Scikit-Learn

FastAPI

Streamlit

Plotly

SHAP

Uvicorn

🚀 Installation & Execution
1️⃣ Clone Repository
git clone https://github.com/pruthvirajtarode789-coder/FraudShield-Real-Time-Fraud-Detection.git
cd FraudShield-Real-Time-Fraud-Detection

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Train ML Model
python training/train_model.py

5️⃣ Start API Server
uvicorn api.app:app --reload


Runs at:

http://127.0.0.1:8000


Swagger:

http://127.0.0.1:8000/docs

6️⃣ Start Streamlit Dashboard
streamlit run app/streamlit_app.py


Runs at:

http://localhost:8501
