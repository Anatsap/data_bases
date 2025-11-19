from typing import List, Dict, Any
from my_project.auth.service.orders import movie_service
from my_project.auth.controller.general_controller import GeneralController

class MovieController(GeneralController):
    _service = movie_service

    def get_actors_by_movie_id_route(self, movie_id: int) -> List[Dict[str, Any]]:
        actors_data = self._service.find_actors_by_movie_id(movie_id)
        return [dict(actor) for actor in actors_data]

movie_controller = MovieController()
