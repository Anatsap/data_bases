from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String

class Director(db.Model, IDto):
    __tablename__ = "directors"

    director_id = db.Column(db.Integer, primary_key=True) 
    first_name = db.Column(db.String(45), nullable=False)
    last_name = db.Column(db.String(45), nullable=False)
    nationality = db.Column(db.String(45))
    imdb_code = db.Column(db.String(20), unique=True, nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.director_id, 
            "first_name": self.first_name, 
            "last_name": self.last_name, 
            "nationality": self.nationality
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'Director':
        return Director(**dto_dict)