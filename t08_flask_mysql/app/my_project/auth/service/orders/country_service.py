
from typing import List, Dict, Any
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService
from t08_flask_mysql.app.my_project.auth.dao.orders import country_dao
from t08_flask_mysql.app.my_project.auth.domain.orders.country import Country

class CountryService(GeneralService):
    _dao = country_dao
    def find_box_office_by_country(self, country_id: int) -> List[Dict[str, Any]]:
        box_office_records = self._dao.find_box_office_by_country(country_id)
        return [record.put_into_dto() for record in box_office_records]