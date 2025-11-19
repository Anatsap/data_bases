
from __future__ import annotations
from typing import Dict, Any
from sqlalchemy.orm import relationship
from my_project import db
from my_project.auth.domain.i_dto import IDto

class Actor(db.Model, IDto):
    __tablename__ = "actors"

    actor_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    last_name = db.Column(db.String(45), nullable=False)
    nationality = db.Column(db.String(45))
    birth_date = db.Column(db.Date)
    bio = db.Column(db.Text)
    imdb_code = db.Column(db.String(20), nullable=False)


    movies_link = relationship("MovieActor", back_populates="actor") 

    def __repr__(self) -> str:
        return f"Actor(id={self.actor_id}, name='{self.name}', nationality='{self.nationality}', birth_date ='{self.birth_date}', bio ='{self.bio}', imdb_code='{self.imdb_code}' )"

    def put_into_dto(self) -> Dict[str, Any]:
        return {"id": self.actor_id, "name": self.name, "nationality": self.nationality, "birth_date": self.birth_date, "bio":self.bio, "imdb_code": self.imdb_code}

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Actor:
        return Actor(**dto_dict)