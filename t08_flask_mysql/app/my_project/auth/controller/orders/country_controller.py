from typing import List, Dict, Any
from t08_flask_mysql.app.my_project.auth.service import country_service 
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class CountryController(GeneralController):
    _service = country_service  
    
    def get_box_office_by_county_route(self, country_id: int) -> List[Dict[str, Any]]:
        box_office_data = self._service.find_box_office_by_country(country_id)
        return list(map(lambda x: dict(x), box_office_data))
    