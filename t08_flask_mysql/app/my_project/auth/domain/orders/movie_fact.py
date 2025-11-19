from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey, Text, String

class MovieFact(db.Model, IDto):
    __tablename__ = "movie_facts"

    fact_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fact_text = db.Column(db.Text, nullable=False)
    source = db.Column(db.String(60))

    movie_id = db.Column(db.Integer, db.ForeignKey('movies.movie_id'), nullable=False)
    
    movie = db.relationship("Movie", back_populates="facts_link") 

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.fact_id, 
            "movie_id": self.movie_id, 
            "fact_text": self.fact_text,
            "source": self.source,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'MovieFact':
        return MovieFact(**dto_dict)