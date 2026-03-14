"""
Roadmap Recommendation Module
"""
import pickle
from typing import Dict, List


class RoadmapRecommender:
    def __init__(self, model_path: str = "models/roadmap_recommender.pkl"):
        self.model = None
        self.model_path = model_path

    def load_model(self):
        try:
            with open(self.model_path, "rb") as f:
                self.model = pickle.load(f)
        except FileNotFoundError:
            print(f"Model not found at {self.model_path}")

    def recommend(self, user_features: Dict) -> Dict:
        """Recommend a learning roadmap"""
        current_level = user_features.get("current_level", "A1")
        weak_skills = self._identify_weak_skills(user_features)

        level_progression = {
            "A1": "A2", "A2": "B1", "B1": "B2",
            "B2": "C1", "C1": "C2", "C2": "C2"
        }

        return {
            "current_level": current_level,
            "target_level": level_progression.get(current_level, "B1"),
            "weak_skills": weak_skills,
            "focus_areas": self._get_focus_areas(weak_skills),
            "estimated_days": self._estimate_duration(current_level),
        }

    def _identify_weak_skills(self, features: Dict) -> List[str]:
        """Identify weak skills based on scores"""
        skills = ["grammar", "vocabulary", "reading", "listening", "speaking", "writing"]
        weak = []
        for skill in skills:
            score = features.get(f"{skill}_avg", 50)
            if score < 60:
                weak.append(skill)
        return weak if weak else ["general"]

    def _get_focus_areas(self, weak_skills: List[str]) -> List[str]:
        suggestions = {
            "grammar": "Practice grammar exercises and rules",
            "vocabulary": "Learn new words daily with flashcards",
            "reading": "Read English articles and stories",
            "listening": "Listen to podcasts and watch videos",
            "speaking": "Practice speaking with conversation exercises",
            "writing": "Write essays and journal entries",
            "general": "Focus on overall English improvement",
        }
        return [suggestions.get(skill, "") for skill in weak_skills]

    def _estimate_duration(self, current_level: str) -> int:
        durations = {"A1": 30, "A2": 45, "B1": 60, "B2": 90, "C1": 120, "C2": 30}
        return durations.get(current_level, 60)
