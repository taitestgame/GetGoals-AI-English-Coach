"""
Level Prediction Module
"""
import pickle
import numpy as np
from typing import Dict, Optional


class LevelPredictor:
    def __init__(self, model_path: str = "models/level_classifier.pkl"):
        self.model = None
        self.model_path = model_path
        self.levels = ["A1", "A2", "B1", "B2", "C1", "C2"]

    def load_model(self):
        """Load trained model"""
        try:
            with open(self.model_path, "rb") as f:
                self.model = pickle.load(f)
        except FileNotFoundError:
            print(f"Model not found at {self.model_path}")

    def predict(self, features: np.ndarray) -> Dict:
        """Predict English level"""
        if self.model is None:
            self.load_model()

        if self.model is None:
            return {"level": "B1", "confidence": 0.5, "message": "Using default prediction"}

        prediction = self.model.predict(features)
        probabilities = self.model.predict_proba(features)
        confidence = float(max(probabilities[0]))

        return {
            "level": prediction[0],
            "confidence": confidence,
            "probabilities": {
                level: float(prob)
                for level, prob in zip(self.model.classes_, probabilities[0])
            },
        }
