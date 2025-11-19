
from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto
from sqlalchemy.orm import relationship
from sqlalchemy import Numeric


class Movie(db.Model, IDto):
    __tablename__ = "movies"

    movie_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(60), nullable=False)
    release_year = db.Column(db.Integer, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text)
    imdb_code = db.Column(db.String(30), nullable=False)
    rating = db.Column(Numeric(3, 1))

    actors_link = db.relationship("MovieActor", back_populates="movie")
    box_office_data = db.relationship("BoxOffice", back_populates="movie")
    
    def __repr__(self) -> str:
        return f"Movie(id={self.movie_id}, title='{self.title}', release_year={self.release_year}, duration={self.duration}, description={self.description}, imdb_code={self.imdb_code}, rating={self.rating})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {"id": self.movie_id, "title": self.title, "release_year": self.release_year, "duration": self.duration, "description": self.description, "imdb_code": self.imdb_code, "rating": self.rating}

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Movie:
        return Movie(**dto_dict)