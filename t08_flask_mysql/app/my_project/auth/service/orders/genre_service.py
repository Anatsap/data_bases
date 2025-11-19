from typing import List, Dict, Any, Optional

from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao.orders.genre_dao import genre_dao
from my_project.auth.domain.orders.genre import Genre
from my_project.auth.domain.orders.movie import Movie



class GenreService(GeneralService):

    _dao = genre_dao

    def find_movies_by_genre_id(self, genre_id: int) -> List[Dict[str, Any]]:
        movies_of_genre: List[Movie] = self._dao.find_movies_by_genre_id(genre_id)
        return [movie.put_into_dto() for movie in movies_of_genre]

    def delete(self, genre_id: int) -> None:
        self._dao.delete(genre_id)

genre_service = GenreService()
