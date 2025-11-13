from __future__ import annotations
from typing import Dict, Any
from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String

class Genre(db.Model, IDto):
    __tablename__ = "genres"

    genre_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)

    movies_link = relationship("MovieGenre", back_populates="genre") 

    def put_into_dto(self) -> Dict[str, Any]:
        return {"id": self.genre_id, "name": self.name}

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'Genre':
        return Genre(**dto_dict)