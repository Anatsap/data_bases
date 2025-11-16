
from typing import List, Dict, Any
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService
from t08_flask_mysql.app.my_project.auth.dao.orders import actor_dao
from t08_flask_mysql.app.my_project.auth.domain.orders.actor import Actor
from t08_flask_mysql.app.my_project.auth.domain.orders.movie import Movie
from typing import List, Dict, Any, Optional

class ActorService(GeneralService):
    _dao = actor_dao

    def find_movies_by_actor_id(self, actor_id: int) -> List[Dict[str, Any]]:
        movies_of_actor: List[Movie] = self._dao.find_movies_by_actor_id(actor_id)
        return [movie.put_into_dto() for movie in movies_of_actor]

    def find_by_nationality(self, nationality: str) -> List[Dict[str, Any]]:
        actors_list: List[Actor] = self._dao.find_by_nationality(nationality)
        return [actor.put_into_dto() for actor in actors_list]

    def remove_actor_from_movie(self, movie_id: int, actor_id: int) -> None:
        self._dao.remove_actor_from_movie(movie_id, actor_id)
        
    def add_movie_to_actor(self, actor_id: int, movie_id: int, character_name: str, billing_order: Optional[int] = None) -> None:
        self._dao.add_movie_to_actor(actor_id, movie_id, character_name, billing_order)

    def delete(self, actor_id: int):
        self._dao.delete(actor_id)




#     def find_movies_by_actor_id(self, actor_id: int) -> List[Movie]:
#         # SQL: SELECT m.*, ma.character_name FROM movies m 
#         #      JOIN movie_actors ma ON m.movie_id = ma.movie_id 
#         #      WHERE ma.actor_id = %s;
#         ...
#
#     def find_by_imdb_code(self, imdb_code: str) -> Optional[Actor]:
#         # SQL: SELECT * FROM actors WHERE imdb_code = %s;
#         ...
#
#     def remove_actor_from_movie(self, movie_id: int, actor_id: int) -> None:
#         # SQL: DELETE FROM movie_actors WHERE movie_id = %s AND actor_id = %s;
#         ...
#
#     def add_movie_to_actor(self, actor_id: int, movie_id: int, character_name: str, billing_order: Optional[int] = None) -> None:
#         # SQL: INSERT INTO movie_actors (movie_id, actor_id, character_name, billing_order) 
#         #      VALUES (%s, %s, %s, %s);
#         ...