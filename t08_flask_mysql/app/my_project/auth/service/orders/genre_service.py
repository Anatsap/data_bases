

from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService
from t08_flask_mysql.app.my_project.auth.dao.orders import genre_dao
from t08_flask_mysql.app.my_project.auth.domain.orders.genre import Genre
from t08_flask_mysql.app.my_project.auth.domain.orders.movie import Movie

from typing import List, Dict, Any, Optional


class GenreService(GeneralService):

    _dao = genre_dao

    def find_movies_by_genre_id(self, genre_id: int) -> List[Dict[str, Any]]:
        movies_of_genre: List[Movie] = self._dao.find_movies_by_genre_id(genre_id)
        return [movie.put_into_dto() for movie in movies_of_genre]

    def delete(self, genre_id: int) -> None:
        self._dao.delete(genre_id)