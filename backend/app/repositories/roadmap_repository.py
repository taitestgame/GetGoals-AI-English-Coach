"""
Roadmap repository
"""
from sqlalchemy.orm import Session
from app.models.roadmap import Roadmap, UserRoadmap


class RoadmapRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, roadmap_id: int):
        return self.db.query(Roadmap).filter(Roadmap.id == roadmap_id).first()

    def get_all(self):
        return self.db.query(Roadmap).all()

    def get_user_roadmaps(self, user_id: int):
        return self.db.query(UserRoadmap).filter(UserRoadmap.user_id == user_id).all()

    def create(self, roadmap: Roadmap):
        self.db.add(roadmap)
        self.db.commit()
        self.db.refresh(roadmap)
        return roadmap
