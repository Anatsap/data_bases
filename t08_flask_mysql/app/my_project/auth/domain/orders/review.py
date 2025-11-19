from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto
from sqlalchemy.orm import relationship
from sqlalchemy import Numeric

class Review(db.Model, IDto):
    __tablename__ = "reviews"

    review_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(45), nullable=False)
    rating = db.Column(Numeric(3, 1))
    comment = db.Column(db.Text)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.movie_id'), nullable=False)
    
    movie = db.relationship("Movie", back_populates="reviews") 

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.review_id, 
            "movie_id": self.movie_id, 
            "user_name": self.user_name,
            "rating": float(self.rating)
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'Review':
        return Review(**dto_dict)