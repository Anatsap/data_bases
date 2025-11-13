
from typing import List, Dict, Any
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService
from t08_flask_mysql.app.my_project.auth.dao.orders import review_dao
from t08_flask_mysql.app.my_project.auth.domain.orders.review import Review
from t08_flask_mysql.app.my_project.auth.domain.orders.movie import Movie
from typing import List, Dict, Any, Optional

class ReviewService(GeneralService):
    _dao = review_dao  

    def find_movies_by_actor_id(self, actor_id: int) -> List[Dict[str, Any]]:
        movies_of_actor: List[Movie] = self._dao.find_movies_by_actor_id(actor_id)
        return [movie.put_into_dto() for movie in movies_of_actor]

    def find_actor_by_imdb_code(self, imdb_code: str) -> Optional[Dict[str, Any]]:
        actor: Optional[Actor] = self._dao.find_by_imdb_code(imdb_code)
        if actor:
            return actor.put_into_dto()
        return None

    def remove_actor_from_movie(self, movie_id: int, actor_id: int) -> None:
        self._dao.remove_actor_from_movie(movie_id, actor_id)
        
    def add_movie_to_actor(self, actor_id: int, movie_id: int, character_name: str, billing_order: Optional[int] = None) -> None:
        self._dao.add_movie_to_actor(actor_id, movie_id, character_name, billing_order)