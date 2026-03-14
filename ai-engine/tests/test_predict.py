"""
Tests for AI prediction module
"""
import pytest
import numpy as np


def test_predict_level_default():
    """Test default level prediction when no model is loaded"""
    from src.predict_level import LevelPredictor
    predictor = LevelPredictor(model_path="nonexistent.pkl")
    result = predictor.predict(np.array([[0.5, 0.6, 0.7, 0.4, 0.3, 0.5, 10, 65]]))
    assert "level" in result
    assert "confidence" in result


def test_feature_engineering():
    """Test feature engineering"""
    from src.feature_engineering import extract_skill_features
    quiz_results = [
        {"category": "grammar", "score": 80},
        {"category": "grammar", "score": 90},
        {"category": "vocabulary", "score": 70},
    ]
    features = extract_skill_features(quiz_results)
    assert "grammar_avg" in features
    assert features["grammar_avg"] == 85.0


def test_preprocess():
    """Test data preprocessing"""
    from src.preprocess import normalize_scores
    scores = [10, 20, 30, 40, 50]
    normalized = normalize_scores(scores)
    assert min(normalized) == 0.0
    assert max(normalized) == 1.0
