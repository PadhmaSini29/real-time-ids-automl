#dashboard.py
from model import IDSModel

import streamlit as st
import requests

st.set_page_config(page_title="Real-Time IDS", layout="wide")
st.title("🔐 Real-time Network Intrusion Detection System")

st.markdown("Simulate a network event:")

# 🎛 Input Fields
col1, col2 = st.columns(2)

with col1:
    dst_port = st.number_input("Dst Port", value=80)
    flow_duration = st.number_input("Flow Duration", value=123456)
    fwd_packets = st.number_input("Fwd Packets", value=10)

with col2:
    protocol = st.selectbox("Protocol", [6, 17], format_func=lambda x: "TCP" if x == 6 else "UDP")
    bwd_packets = st.number_input("Bwd Packets", value=8)
    label = st.selectbox("Label (0 = Benign, 1 = Attack)", ["0", "1"])

# 📤 Submit and Send to API
if st.button("🚀 Predict"):
    features = {
        "Dst Port": dst_port,
        "Protocol": protocol,
        "Flow Duration": flow_duration,
        "Fwd Packets": fwd_packets,
        "Bwd Packets": bwd_packets
    }

    try:
        response = requests.post("http://localhost:5000/predict", json={
            "features": features,
            "label": label
        })

        if response.status_code == 200:
            result = response.json()
            st.success(f"🧠 Prediction: {result['prediction']}")
            st.metric("📈 Accuracy", result['accuracy'])
            if result['drift_detected']:
                st.error("⚠️ Drift Detected!")
            else:
                st.success("✅ No Drift Detected")
        else:
            st.error("❌ API Error: " + response.text)

    except Exception as e:
        st.error("🔌 Could not connect to API: " + str(e))
