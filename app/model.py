from river.ensemble import LeveragingBaggingClassifier
from river.tree import HoeffdingTreeClassifier
from river.metrics import Accuracy
from river.drift import ADWIN

class IDSModel:
    def __init__(self):
        base_model = HoeffdingTreeClassifier()
        self.model = LeveragingBaggingClassifier(model=base_model)
        self.metric = Accuracy()
        self.drift_detector = ADWIN()

    def predict_and_update(self, x, y):
        y_pred = self.model.predict_one(x)

        if y_pred is None:
            y_pred = "UNKNOWN"
        else:
            y_pred = str(y_pred)

        self.model.learn_one(x, y)
        self.metric.update(y, y_pred)

        drift_detected = bool(self.drift_detector.update(int(y != y_pred)))
        accuracy_score = float(self.metric.get())
        return y_pred, drift_detected, accuracy_score

    def warm_up(self, data_iterable):
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
