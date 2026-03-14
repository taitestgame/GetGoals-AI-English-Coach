"""
Feature Engineering for AI models
"""
import pandas as pd
import numpy as np
from typing import Dict, List


def extract_skill_features(quiz_results: List[Dict]) -> Dict:
    """Extract skill-level features from quiz results"""
    skill_scores = {
        "grammar": [],
        "vocabulary": [],
        "reading": [],
        "listening": [],
        "speaking": [],
        "writing": [],
    }

    for result in quiz_results:
        category = result.get("category", "")
        score = result.get("score", 0)
        if category in skill_scores:
            skill_scores[category].append(score)

    features = {}
    for skill, scores in skill_scores.items():
        features[f"{skill}_avg"] = np.mean(scores) if scores else 0
        features[f"{skill}_count"] = len(scores)
        features[f"{skill}_trend"] = calculate_trend(scores) if len(scores) > 1 else 0

    return features


def calculate_trend(scores: List[float]) -> float:
    """Calculate improvement trend (positive = improving)"""
    if len(scores) < 2:
        return 0.0
    recent = scores[-3:]
    older = scores[:-3] if len(scores) > 3 else scores[:1]
    return np.mean(recent) - np.mean(older)


def create_feature_matrix(users_data: List[Dict]) -> pd.DataFrame:
    """Create feature matrix from multiple users' data"""
    features_list = []
    for user_data in users_data:
        features = extract_skill_features(user_data.get("quiz_results", []))
        features["user_id"] = user_data.get("user_id")
        features_list.append(features)

    return pd.DataFrame(features_list)
