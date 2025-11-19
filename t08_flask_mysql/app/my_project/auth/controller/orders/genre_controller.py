
from typing import List, Dict, Any
from my_project.auth.service.orders import genre_service 
from my_project.auth.controller.general_controller import GeneralController


class GenreController(GeneralController):
    _service = genre_service  
    
    def get_movies_by_genre_id_route(self, genre_id: int) -> List[Dict[str, Any]]:
        movies_genres_data = self._service.find_movies_by_genre_id(genre_id)
        return list(map(lambda x: dict(x), movies_genres_data))
