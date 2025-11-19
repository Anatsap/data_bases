from typing import List
from my_project import db
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.movie import Movie
from my_project.auth.domain.orders.actor import Actor
from my_project.auth.domain.orders.movie_actor import MovieActor

class MovieDAO(GeneralDAO):
    _domain_type = Movie

    def find_actors_by_movie_id(self, movie_id: int) -> List[Actor]:
        session = db.session
        return session.query(Actor).join(MovieActor).filter(MovieActor.movie_id == movie_id).all()

movie_dao = MovieDAO()
