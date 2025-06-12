# 🔐 Real-Time Intrusion Detection System (IDS) using AutoML

A real-time, stream-based Intrusion Detection System built using Python, River (online learning), Flask (API), and Streamlit (dashboard).  
Trained on the CICIDS2017 dataset, this system uses adaptive machine learning and drift detection to identify network threats in real time.

---

## 🚀 Features

- ✅ **Online Learning** with Adaptive Random Forest (River)
- 🔄 **Model Warm-Up** using CICIDS2017 sample data
- ⚠️ **Drift Detection** via ADWIN algorithm
- 📊 **Interactive Dashboard** built with Streamlit
- 🔌 **REST API** for real-time prediction
- 📈 **Live Accuracy and Prediction Tracking**

---

## 🧠 Tech Stack

- **Python 3.8+**
- [River](https://riverml.xyz/) – stream learning
- Flask – API layer
- Streamlit – frontend dashboard
- pandas – data manipulation
- scikit-learn – optional batch learning

---

## 📂 Project Structure

ids-project/
├── api.py # Flask API backend
├── model.py # Online ML model class (AutoML + drift)
├── dashboard.py # Streamlit UI for testing and visualization
├── data/
│ └── cic_0.01km.csv # Sample CICIDS2017 data
├── requirements.txt # Dependencies
└── README.md # Project overview

