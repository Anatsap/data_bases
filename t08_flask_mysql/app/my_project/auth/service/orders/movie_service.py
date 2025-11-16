
from typing import List, Dict, Any
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService
from t08_flask_mysql.app.my_project.auth.dao.orders import movie_dao
from t08_flask_mysql.app.my_project.auth.domain.orders.movie import Movie
from t08_flask_mysql.app.my_project.auth.domain.orders.actor import Actor 

class MovieService(GeneralService):
    _dao = movie_dao

    def find_actors_by_movie_id(self, movie_id: int) -> List[Dict[str, Any]]:
        actors_in_movie: List[Actor] = self._dao.find_actors_by_movie_id(movie_id)
        return [actor.put_into_dto() for actor in actors_in_movie]

    def add_actor_to_movie(self, movie_id: int, actor_id: int, character_name: str) -> None:
        self._dao.add_actor_to_movie(movie_id, actor_id, character_name)

    def delete(self, movie_id: int) -> None:
        self._dao.delete(movie_id)