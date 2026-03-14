"""
Roadmap service
"""
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.roadmap import Roadmap, UserRoadmap


class RoadmapService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_roadmaps(self):
        return self.db.query(Roadmap).all()

    def get_user_roadmap(self, user_id: int):
        user_roadmap = self.db.query(UserRoadmap).filter(
            UserRoadmap.user_id == user_id,
            UserRoadmap.status == "active",
        ).first()
        if not user_roadmap:
            raise HTTPException(status_code=404, detail="No active roadmap found")
        roadmap = self.db.query(Roadmap).filter(Roadmap.id == user_roadmap.roadmap_id).first()
        return {"roadmap": roadmap, "progress": user_roadmap.progress, "current_milestone": user_roadmap.current_milestone}

    def enroll_user(self, user_id: int, roadmap_id: int):
        roadmap = self.db.query(Roadmap).filter(Roadmap.id == roadmap_id).first()
        if not roadmap:
            raise HTTPException(status_code=404, detail="Roadmap not found")

        existing = self.db.query(UserRoadmap).filter(
            UserRoadmap.user_id == user_id,
            UserRoadmap.roadmap_id == roadmap_id,
        ).first()
        if existing:
            raise HTTPException(status_code=400, detail="Already enrolled in this roadmap")

        user_roadmap = UserRoadmap(user_id=user_id, roadmap_id=roadmap_id)
        self.db.add(user_roadmap)
        self.db.commit()
        return {"message": "Successfully enrolled in roadmap"}

    def update_progress(self, user_id: int, roadmap_id: int, progress: dict):
        user_roadmap = self.db.query(UserRoadmap).filter(
            UserRoadmap.user_id == user_id,
            UserRoadmap.roadmap_id == roadmap_id,
        ).first()
        if not user_roadmap:
            raise HTTPException(status_code=404, detail="Enrollment not found")

        if "progress" in progress:
            user_roadmap.progress = progress["progress"]
        if "current_milestone" in progress:
            user_roadmap.current_milestone = progress["current_milestone"]
        self.db.commit()
        return {"message": "Progress updated"}
