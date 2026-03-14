"""
Model Training Script
"""
import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import json


def train_level_classifier(X, y, model_path="models/level_classifier.pkl"):
    """Train English level classifier"""
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred, output_dict=True)

    # Save model
    with open(model_path, "wb") as f:
        pickle.dump(model, f)

    print(f"Model saved to {model_path}")
    print(f"Accuracy: {report['accuracy']:.4f}")

    return model, report


def train_roadmap_recommender(X, y, model_path="models/roadmap_recommender.pkl"):
    """Train roadmap recommendation model"""
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = GradientBoostingClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Save model
    with open(model_path, "wb") as f:
        pickle.dump(model, f)

    print(f"Recommender model saved to {model_path}")
    return model


def save_metadata(metadata: dict, path="models/metadata.json"):
    """Save model metadata"""
    with open(path, "w") as f:
        json.dump(metadata, f, indent=2)


if __name__ == "__main__":
    # Example training with dummy data
    print("Training models...")
    # TODO: Replace with actual training data
    X_dummy = np.random.rand(100, 8)
    y_dummy = np.random.choice(["A1", "A2", "B1", "B2", "C1", "C2"], 100)

    model, report = train_level_classifier(X_dummy, y_dummy)
    save_metadata({"version": "1.0", "features": 8, "accuracy": report["accuracy"]})
    print("Training complete!")
