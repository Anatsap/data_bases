
from typing import List
from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain.orders.country import Country

class CountryDAO(GeneralDAO):
    _domain_type = Country
    def find_country_by_country_id(self, country_id: int) -> List[Country]:
        session = db.session
        return session.query(Country).filter(Country.country_id == country_id).all()