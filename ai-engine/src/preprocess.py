"""
Data Preprocessing for AI Engine
"""
import pandas as pd
import numpy as np
from typing import List, Dict


def load_data(filepath: str) -> pd.DataFrame:
    """Load raw data from file"""
    return pd.read_csv(filepath)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and preprocess raw data"""
    # Remove duplicates
    df = df.drop_duplicates()
    # Handle missing values
    df = df.fillna(0)
    return df


def normalize_scores(scores: List[float]) -> List[float]:
    """Normalize scores to 0-1 range"""
    min_val = min(scores) if scores else 0
    max_val = max(scores) if scores else 1
    if max_val == min_val:
        return [0.5] * len(scores)
    return [(s - min_val) / (max_val - min_val) for s in scores]


def prepare_features(user_data: Dict) -> np.ndarray:
    """Prepare features for ML model input"""
    features = [
        user_data.get("grammar_score", 0),
        user_data.get("vocabulary_score", 0),
        user_data.get("reading_score", 0),
        user_data.get("listening_score", 0),
        user_data.get("speaking_score", 0),
        user_data.get("writing_score", 0),
        user_data.get("total_quizzes", 0),
        user_data.get("avg_score", 0),
    ]
    return np.array(features).reshape(1, -1)
