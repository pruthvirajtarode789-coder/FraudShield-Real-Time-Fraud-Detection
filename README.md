🛡️ FraudShield — Real-Time Fraud Detection System

Enterprise-grade AI system for real-time transaction fraud prevention

FraudShield is a machine learning powered fraud detection platform designed to help banks, fintech companies, and digital payment platforms detect and prevent fraudulent transactions instantly.
The system provides real-time fraud prediction, an interactive dashboard, and a production-ready API.

🚀 Live Capabilities

✅ Real-time Fraud Prediction
✅ AI Risk Scoring
✅ Production-ready FastAPI
✅ Interactive Streamlit Dashboard
✅ Cloud Deployable
✅ Client-ready Architecture
✅ Fully Modular ML System

🧠 Functional Overview

FraudShield consists of three major components:

Training Module

Trains a Machine Learning model using transaction data

Performs feature engineering and saves trained model

FastAPI Prediction Server

Hosts the trained ML model

Exposes /predict API for real-time inference

Streamlit Web Dashboard

Allows users to enter transaction details

Displays fraud probability with visual analytics

📂 Project Structure
FraudShield-Full-Project/
│
├── api/                   # FastAPI Backend
│   └── app.py
│
├── app/                   # Streamlit Dashboard
│   └── streamlit_app.py
│
├── training/              # Model Training
│   └── train_model.py
│
├── models/                # Saved ML Models
│   ├── fraud_model.pkl
│   ├── model_columns.json
│   └── feature_importance.json
│
├── data/raw/              # Training Data
│   └── fraud_transactions_sample.csv
│
├── diagrams/              # System Diagrams
│
├── requirements.txt      # All Dependencies
├── README.md              # Project Documentation
└── generate_diagrams.py

🔗 Tech Stack

Programming Language: Python

Machine Learning: Scikit-Learn

API Backend: FastAPI + Uvicorn

Frontend: Streamlit

Visualization: Plotly

Explainability (Optional): SHAP

Deployment: Streamlit Cloud / Local Server

⚙️ Installation & Setup
✅ 1. Clone Repository
git clone https://github.com/pruthvirajtarode789-coder/FraudShield-Real-Time-Fraud-Detection.git
cd FraudShield-Real-Time-Fraud-Detection

✅ 2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate

✅ 3. Install Dependencies
pip install -r requirements.txt

✅ 4. Train the Model
python training/train_model.py


This generates:

models/fraud_model.pkl

models/model_columns.json

models/feature_importance.json

✅ 5. Start FastAPI Server
uvicorn api.app:app --reload


API will run at:

http://127.0.0.1:8000


Swagger Docs:

http://127.0.0.1:8000/docs

✅ 6. Start Streamlit Dashboard
streamlit run app/streamlit_app.py


Dashboard will run at:

http://localhost:8501

🎯 Sample Prediction Input
Feature	Example
Amount	5000
Transaction Type	Withdrawal
Channel	Mobile
Country	India
Time of Day	Morning
Device Type	Android
✅ Output

Fraud Probability (%)

Risk Label: SAFE / FRAUD

Confidence Visualization

📊 System Diagrams
🎯 1. Use Case Diagram
+-------------------+         +-------------------+
|  Data Scientist   |         |     End User      |
+-------------------+         +-------------------+
          |                             |
          v                             v
     +----------+                 +-------------+
     | Train ML |                 | Input       |
     | Model    |                 | Transaction |
     +----------+                 +-------------+
          |                             |
          v                             v
     +-----------+    +----------------+    +-------------+
     | Deploy    |<---|  FraudShield   |--->| Analyze     |
     | Model     |    |    System      |    | Transaction |
     +-----------+    +----------------+    +-------------+
          ^
          |
   +----------------+
   | System Admin   |
   +----------------+
          |
          v
     +----------------+
     | View Risk &    |
     | Export Reports |
     +----------------+

🔄 2. Sequence Diagram
User        Streamlit App      FastAPI Server       ML Model
 |              |                  |                   |
 |---Open App-->|                  |                   |
 |---Enter Data------------------>|                   |
 |              |---POST /predict------------------->|
 |              |                  |--Load Model---->|
 |              |                  |--Preprocess---->|
 |              |                  |--Predict------>|
 |              |                  |<--Result--------|
 |<--Display Result--------------|                   |

🏗️ 3. Architecture Diagram
Streamlit UI  →  FastAPI  →  ML Model  →  Prediction Output

📊 4. Data Flow Diagram
CSV Data → Training → Model → API → Streamlit → User

🔧 5. Component Diagram
Training Module → API Module → UI Module → Prediction Output

🌐 6. Deployment Diagram
Local System / Cloud → API + Streamlit → User Browser

📈 7. Activity Diagram
Start → Enter Data → Validate → Predict → Display → End

📋 8. Class Diagram
StreamlitUI → FraudDetector → ModelManager → ML Model

✅ Project Applications

Banking Fraud Detection

Credit Card Fraud Analysis

Digital Payment Security

Fintech Risk Assessment

Real-time Transaction Monitoring

🏆 Project Highlights

✅ Real-World Use Case
✅ Production-ready API
✅ Fully Deployable
✅ Live Prediction
✅ Client Dashboard
✅ ML + Web Integration
✅ Internship / Placement Ready

👨‍💻 Developed By

Pruthviraj Tarode
B.Tech CSE | AI/ML & Data Science
Fraud & Risk Analytics Engineer

📜 License
