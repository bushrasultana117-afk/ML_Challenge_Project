# ML_Challenge_Project

# 🚨 SentinelAI — AI-Powered Industrial Machine Health Monitoring

SentinelAI is an **AI-powered industrial machine health monitoring system** designed to detect abnormal machine conditions using real-time sensor data.

The system analyzes:

* 🌡️ Temperature
* 📳 Vibration
* 💧 Humidity
* 🎚️ Pressure
* ⚡ Energy Consumption

SentinelAI combines **Machine Learning, FastAPI, Streamlit, and** to provide machine health predictions through an interactive dashboard.

---

## 🔗 Production API

The Streamlit application communicates with the deployed FastAPI backend using the production API:

```python
API_URL = "https://ml-challenge-project.onrender.com"
```

🚀 Streamlit Dashboard

Try the live Streamlit dashboard and explore the SentinelAI application.

https://ml-challenge-project-bs.streamlit.app/
```

---

## 🚀 Project Overview

SentinelAI follows this pipeline:

```text
Industrial Sensor Data
        ↓
Data Preprocessing
        ↓
Machine Learning Model
        ↓
FastAPI Backend
        ↓
Streamlit Dashboard
        ↓
Machine Health Prediction
```

The system classifies machines as:

* ✅ **NORMAL**
* 🚨 **ANOMALY**

It can also provide anomaly scores, thresholds, and maintenance recommendations.

---

# 🧠 Machine Learning

Several machine learning algorithms were evaluated during development:

1. Logistic Regression
2. Random Forest
3. XGBoost
4. Isolation Forest


The final supervised classification model selected for SentinelAI is **Random Forest**.

---

# 📊 Model Performance

## Logistic Regression

| Metric    |      Score |
| --------- | ---------: |
| Accuracy  | **84.44%** |
| Precision | **35.04%** |
| Recall    | **87.32%** |
| F1 Score  | **50.01%** |

Logistic Regression achieved good recall but had lower precision compared with Random Forest.

---

## 🌲 Random Forest

| Metric    |       Score |
| --------- | ----------: |
| Accuracy  |  **99.98%** |
| Precision |  **99.78%** |
| Recall    | **100.00%** |
| F1 Score  |  **99.89%** |



---

## ⚡ XGBoost

XGBoost was also evaluated during model development.

| Metric    | Score |
| --------- | ----: |
| Accuracy  |   TBD |
| Precision |   TBD |
| Recall    |   TBD |
| F1 Score  |   TBD |

> XGBoost metrics will be added once the final experiment results are confirmed.

---

# 🔍 Unsupervised Anomaly Detection

Additional anomaly detection algorithms were investigated during development.

## Isolation Forest

| Metric    |  Score |
| --------- | -----: |
| Precision | 35.23% |
| Recall    | 26.28% |
| F1 Score  | 30.11% |

---



---

# 📂 Dataset

The project uses industrial smart manufacturing sensor data containing approximately **100,000 records**.

### Dataset Features

| Feature                    | Description                      |
| -------------------------- | -------------------------------- |
| `timestamp`                | Sensor reading timestamp         |
| `machine_id`               | Unique machine identifier        |
| `temperature`              | Machine temperature              |
| `vibration`                | Machine vibration level          |
| `humidity`                 | Environmental humidity           |
| `pressure`                 | Machine/system pressure          |
| `energy_consumption`       | Energy consumed                  |
| `machine_status`           | Machine operating status         |
| `anomaly_flag`             | Actual anomaly indicator         |
| `predicted_remaining_life` | Estimated remaining machine life |
| `failure_type`             | Type of machine failure          |
| `downtime_risk`            | Estimated downtime risk          |
| `maintenance_required`     | Maintenance requirement          |

---

# 🧪 Machine Learning Features

The primary features used by the ML pipeline are:

```text
temperature
vibration
humidity
pressure
energy_consumption
```

---

# ⚙️ Technology Stack

### Backend

* Python
* FastAPI
* Uvicorn
* Pydantic
* Joblib

### Machine Learning

* Scikit-learn
* Random Forest
* Logistic Regression
* XGBoost
* Isolation Forest
* Pandas
* NumPy

### Frontend

* Streamlit


### Deployment

* Render
* Streamlit
* GitHub

---

# 🔌 FastAPI Backend

The FastAPI backend provides REST API endpoints for machine predictions.



```

# 🖥️ Streamlit Dashboard

The Streamlit dashboard provides an interactive interface for machine health monitoring.

Users can enter:

* Factory Name
* Machine ID
* Temperature
* Vibration
* Humidity
* Pressure
* Energy Consumption

The dashboard sends the sensor data to the FastAPI backend.

```text
Streamlit
    ↓
POST /predict
    ↓
FastAPI
    ↓
Random Forest Model
    ↓
Prediction
    ↓
Streamlit
```

---

# 🏆 Final Model

The final supervised learning model used by SentinelAI is:

```text
Random Forest Classifier
```

### Performance

```text
Accuracy  : 99.98%
Precision : 99.78%
Recall    : 100.00%
F1 Score  : 99.89%
```

The trained pipeline is stored at:

```text
sentinel_random_forest_pipeline.pkl
```

---

# 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

### 2. Move into the project directory

```bash
cd SentinelAI
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment on Windows

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run FastAPI Locally

Start the backend:

```bash
uvicorn backend.main:app --reload
```

API:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

---

# ▶️ Run Streamlit Locally

```bash
streamlit run app.py
```

The dashboard will open in your browser.

---

# ☁️ Deployment

SentinelAI uses separate services for the backend and frontend.

### Backend — Render

The FastAPI backend is deployed as a web service on Render.

### Frontend — Streamlit

The Streamlit dashboard is deployed separately and communicates with the production FastAPI API.

### Source Code — GitHub

GitHub is used for source-code management and deployment workflows.

---

# 🔄 Deployment Architecture

```text
                         GitHub
                           │
              ┌────────────┴────────────┐
              ↓                         ↓
           Render                   Streamlit
        FastAPI Backend              Cloud
              │                         │
              │                  User Dashboard
              │                         │
              └────────── API ──────────┘
                           │
                           ↓
                    Random Forest
                        Model
                           │
                           ↓
                   Machine Prediction
```

---

# 🎯 Key Features

* 🤖 AI-powered machine monitoring
* 🌡️ Real-time sensor analysis
* 🚨 Anomaly detection
* 📊 Interactive Streamlit dashboard
* ⚡ FastAPI REST API
* ☁️ Cloud deployment
* 🔧 Maintenance recommendations

---

---

# 👨‍💻 Project Goal

The goal of SentinelAI is to demonstrate how **Artificial Intelligence, Machine Learning, APIs, and modern dashboards** can be combined to build a practical industrial monitoring system.

SentinelAI aims to move machine maintenance from a **reactive approach** toward a more **predictive and data-driven approach**.

---

## ⭐ Built With

```text
Python
FastAPI
Scikit-learn
Random Forest
Streamlit
GitHub
Render
```
