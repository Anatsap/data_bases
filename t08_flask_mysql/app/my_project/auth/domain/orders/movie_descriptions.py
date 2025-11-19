from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey, Text, String

class MovieDescriptions(db.Model, IDto):
    __tablename__ = "movie_descriptions"

    description_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    full_description = db.Column(db.Text)
    keyword = db.Column(db.String(100))
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.movie_id'), unique=True, nullable=False)
    
    movie = db.relationship("Movie", back_populates="description_link") 

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.description_id, 
            "movie_id": self.movie_id, 
            "full_description": self.full_description,
            "keyword": self.keyword,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'MovieDescriptions':
        return MovieDescriptions(**dto_dict)