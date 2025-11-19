
from typing import List, Dict, Any
from my_project import db
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.genre import Genre
from my_project.auth.domain.orders.movie import Movie
from my_project.auth.domain.orders.movie_genre import MovieGenre



class GenreDAO(GeneralDAO):
    _domain_type = Genre
    def find_movies_by_genre_id(self, genre_id: int) -> List[Movie]:
        session = db.session
        movies = session.query(Movie).join(MovieGenre).filter(MovieGenre.genre_id == genre_id).all()
        return movies
    
genre_dao = GenreDAO()