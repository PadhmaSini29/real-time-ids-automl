#api.py

from model import IDSModel

from flask import Flask, request, jsonify

import pandas as pd

app = Flask(__name__)
ids_model = IDSModel()

# 🔄 Step 1: Warm-up the model using your CSV
try:
    df = pd.read_csv("data/cic_0.01km.csv")
    df = df.dropna()

    # 🔍 Show available columns
    print("🧾 CSV Columns:")
    print(df.columns.tolist())

    # ✅ Rename only what's necessary
    df = df.rename(columns={
        'Labelb': 'Label',
        # Update these two lines to match EXACT column names from your CSV:
        'Fwd Packets/s': 'Fwd Packets',
        'Bwd Packets/s': 'Bwd Packets'
    })

    # Add expected features for frontend/API compatibility
    df["Dst Port"] = 80
    df["Protocol"] = 6

    # ✅ Match feature names used in your Streamlit dashboard
    feature_cols = ["Dst Port", "Protocol", "Flow Duration", "Fwd Packets", "Bwd Packets"]
    label_col = "Label"

    # Build warm-up data
    warmup_data = [
        (
            row[feature_cols].to_dict(),
            str(row[label_col])
        )
        for _, row in df.iterrows()
    ]

    print(f"🔥 Warming up model with {len(warmup_data)} records...")
    ids_model.warm_up(warmup_data)
    print("✅ Model warm-up complete.\n")
    print("📌 Sample learned input:", warmup_data[0])

except Exception as e:
    print("⚠️ Skipping warm-up due to error:", str(e))


# 🚀 Step 2: API endpoint for prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = data.get('features', {})
        label = data.get('label', "0").strip().upper()

        # Optional label mapping
        label_map = {"BENIGN": "0", "ATTACK": "1"}
        label = label_map.get(label, label)

        if not features:
            return jsonify({"error": "Missing features in request"}), 400

        y_pred, drift, accuracy = ids_model.predict_and_update(features, label)

        # Debug log
        print(f"[PREDICT] Features: {features} | Label: {label} | Predicted: {y_pred} | Accuracy: {accuracy:.4f}")

        return jsonify({
            "prediction": y_pred,
            "drift_detected": bool(drift),
            "accuracy": round(accuracy, 4)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ✅ Root endpoint
@app.route('/')
def home():
    return "✅ Flask API for Real-Time IDS is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
