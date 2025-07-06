# tests/test_model.py
import unittest
from app.model import IDSModel

class TestIDSModel(unittest.TestCase):
    def test_prediction(self):
        model = IDSModel()
        x = {"Dst Port": 80, "Protocol": 6, "Flow Duration": 1000, "Fwd Packets": 10, "Bwd Packets": 8}
        y = "0"
        model.warm_up([(x, y)])
        pred, drift, acc = model.predict_and_update(x, y)
        self.assertIn(pred, ["0", "1", "UNKNOWN"])

if __name__ == "__main__":
    unittest.main()
