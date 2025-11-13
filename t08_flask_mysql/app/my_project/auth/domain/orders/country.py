
from t08_flask_mysql.app.my_project.auth import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto
from typing import Dict, Any
from sqlalchemy.orm import relationship

class Country(db.Model, IDto):
    __tablename__ = "country"
    country_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country_name = db.Column(db.String(45), unique=True, nullable=False)

    box_office_records = relationship("BoxOffice", back_populates="country") 
    def __repr__(self) -> str:
        return f"Country(country_id={self.country_id}, country_name='{self.country_name}')"

    def put_into_dto(self):
        return {"id": self.country_id, "name": self.country_name}
    
    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'Country':
        return Country(**dto_dict)