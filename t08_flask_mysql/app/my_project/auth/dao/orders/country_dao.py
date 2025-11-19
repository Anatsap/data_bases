
from typing import List
from my_project import db
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.country import Country
from my_project.auth.domain.orders.box_office import BoxOffice

class CountryDAO(GeneralDAO):
    _domain_type = Country

    def find_box_office_by_country(self, country_id: int) -> List[Country]:
        session = db.session
        return session.query(BoxOffice).filter(BoxOffice.country_id == country_id).all()
    
country_dao = CountryDAO()