
# 🔐 Real-Time Intrusion Detection System (IDS) 

A real-time, online-learning-based Intrusion Detection System that uses:
- **Flask** for the backend API
- **Streamlit** for the interactive dashboard
- **River** for online machine learning and drift detection
- **Evidently AI** for data drift monitoring and reporting
- **Prometheus + Grafana** for metrics-based observability
- **Docker** and **GitHub Actions** ready for deployment

---

## 🚀 Features

✅ Online learning model with `AdaptiveRandomForestClassifier`  
✅ Real-time prediction API with Flask  
✅ Drift detection via `ADWIN`  
✅ User-friendly UI with Streamlit  
✅ Data drift reports using Evidently  
✅ Metrics exposed via `/metrics` for Prometheus  
✅ Containerized with Docker  
✅ Ready for CI/CD with GitHub Actions  

---

## 🗂️ Project Structure

```
ids-project/
├── app/
│   ├── api.py                # Flask API
│   ├── model.py              # Online ML model (River)
│   └── dashboard.py          # Streamlit frontend
├── data/
│   └── cic_0.01km.csv        # Sample network dataset
├── reports/
│   └── latest_drift_report.html # Drift report (generated)
├── drift_check.py            # Generates drift report
├── prometheus.yml            # Prometheus config
├── docker-compose.yml        # Prometheus + Grafana stack
├── requirements.txt
├── README.md
```

---

## ⚙️ Setup Instructions

### 🔹 1. Clone the Repo
```bash
git clone https://github.com/yourusername/ids-project.git
cd ids-project
```

### 🔹 2. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🧪 Run Locally

### ▶️ Start Flask API
```bash
cd app
python api.py
```

### ▶️ Start Streamlit Dashboard
```bash
streamlit run app/dashboard.py
```

- Access at: [http://localhost:8501](http://localhost:8501)

---

## 📊 Drift Report (Evidently)

To generate and view the drift report:

```bash
python drift_check.py
```

Or directly from the dashboard:
- Click **🧪 Generate Drift Report**
- Scroll to view 📊 the embedded report

---

## 📈 Monitoring with Prometheus + Grafana

### ▶️ Start Monitoring Stack
```bash
docker-compose up
```

- Prometheus: [http://localhost:9090](http://localhost:9090)  
- Grafana: [http://localhost:3000](http://localhost:3000) (Default login: admin / admin)

### ▶️ Metrics Exposed at:
```bash
http://localhost:5000/metrics
```

Metrics include:
- `ids_predictions_total`
- `ids_drift_total`
- `ids_accuracy`

---

## 📦 Deployment

### 🟡 Streamlit Cloud (Frontend)
- Deploy `app/dashboard.py` from GitHub

### 🔵 Render.com (API)
- Deploy `app/api.py` as a Flask service
- Update dashboard to point to public API endpoint
https://real-time-ids-automl.onrender.com/
---

## ✅ Example Input & Output

**Input (features from dashboard):**
```json
{
  "features": {
    "Dst Port": 80,
    "Protocol": 6,
    "Flow Duration": 123456,
    "Fwd Packets": 10,
    "Bwd Packets": 8
  },
  "label": "0"
}
```

**Output from API:**
```json
{
  "prediction": "0",
  "drift_detected": false,
  "accuracy": 0.9333
}
```

---

## ✅ Requirements

```txt
flask
streamlit
requests
pandas
river
evidently==0.3.3
prometheus_client
```

---


## 🧠 Credits

Built as an MLOps learning project for:
- Stream processing
- Real-time feedback loops
- Production-ready monitoring and deployment

