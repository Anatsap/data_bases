
from typing import Dict, Any
from sqlalchemy.orm import relationship
from sqlalchemy import Numeric


from my_project import db
from my_project.auth.domain.i_dto import IDto

class BoxOffice(db.Model, IDto):
    __tablename__ = "box_office"
    box_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'))
    country_id = db.Column(db.Integer, nullable=False)
    amount = db.Column(Numeric(12, 2))

    country = db.relationship("Country", back_populates="box_office_records") 
    movie = db.relationship("Movie", back_populates="box_office_data")

    def put_into_dto(self):
        return {"box_id": self.box_id, "movie_id": self.movie_id, "country_id": self.country_id, "amount": float(self.amount)}
    
    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'BoxOffice':
        return BoxOffice(**dto_dict)