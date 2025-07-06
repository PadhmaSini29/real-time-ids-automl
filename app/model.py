#model.py

from river.ensemble.adaptive_random_forest import AdaptiveRandomForestClassifier
from river.metrics import Accuracy
from river.drift import ADWIN

class IDSModel:
    def __init__(self):
        self.model = AdaptiveRandomForestClassifier()
        self.metric = Accuracy()
        self.drift_detector = ADWIN()

    def predict_and_update(self, x, y):
        """
        Predict, learn, and update drift detector and accuracy.
        """
        # Predict from model
        y_pred = self.model.predict_one(x)

        # If model hasn't learned yet, return UNKNOWN
        if y_pred is None:
            y_pred = "UNKNOWN"
        else:
            y_pred = str(y_pred)  # Ensure it's serializable

        # Learn from new data point
        self.model.learn_one(x, y)
        self.metric.update(y, y_pred)

        # Update drift detector (1 if incorrect prediction)
        drift_detected = bool(self.drift_detector.update(int(y != y_pred)))

        # Return safe types
        accuracy_score = float(self.metric.get())
        return y_pred, drift_detected, accuracy_score

    def warm_up(self, data_iterable):
        """
        Pre-train the model with labeled data.
        """
        print("🔁 Starting warm-up training...")
        count = 0

        for x, y in data_iterable:
            self.model.learn_one(x, y)
            pred = self.model.predict_one(x)
            self.metric.update(y, pred)

            if count < 5:
                print(f"[WARM-UP] Trained on: {x} => {y} | Predicted: {pred}")
            count += 1

        print(f"✅ Warm-up complete. Total: {count} records")
        print(f"📈 Warm-up Accuracy: {self.metric.get():.4f}")
