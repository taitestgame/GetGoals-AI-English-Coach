"""
Model Export Module
"""
import pickle
import json
from datetime import datetime


def export_model(model, filepath: str, metadata: dict = None):
    """Export trained model to file"""
    with open(filepath, "wb") as f:
        pickle.dump(model, f)

    if metadata:
        meta_path = filepath.replace(".pkl", "_metadata.json")
        metadata["exported_at"] = datetime.now().isoformat()
        with open(meta_path, "w") as f:
            json.dump(metadata, f, indent=2)

    print(f"Model exported to {filepath}")


def load_model(filepath: str):
    """Load model from file"""
    with open(filepath, "rb") as f:
        return pickle.load(f)
