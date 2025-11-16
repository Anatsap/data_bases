
from typing import List
from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain.orders.country import Country
from t08_flask_mysql.app.my_project.auth.domain.orders.box_office import BoxOffice


class CountryDAO(GeneralDAO):
    _domain_type = Country

    def find_box_office_by_country(self, country_id: int) -> List[Country]:
        session = db.session
        return session.query(BoxOffice).filter(BoxOffice.country_id == country_id).all()