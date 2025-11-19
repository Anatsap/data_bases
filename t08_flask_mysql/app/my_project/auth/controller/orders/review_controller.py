from typing import List, Dict, Any
from my_project.auth.service.orders import review_service 
from my_project.auth.controller.general_controller import GeneralController

class ReviewController(GeneralController):
    _service = review_service  
        
    def get_movie_by_review_id_route(self, review_id: int) -> Dict[str, Any]:
        review_dto = self._service.find_movie_by_review_id(review_id)
        if review_dto:
            return review_dto
        return {}
