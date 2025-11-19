"""
©2022-2023 Andrii Pavelchak, apavelchak@gmail.com
Realisation of Actor data access layer.
"""

from typing import List, Optional
from my_project import db
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.actor import Actor
from my_project.auth.domain.orders.movie_actor import MovieActor
from my_project.auth.domain.orders.movie import Movie
import sqlalchemy

import sqlalchemy

class ActorDAO(GeneralDAO):
    _domain_type = Actor
    def find_movies_by_actor_id(self, actor_id: int) -> List[Movie]:
        session = db.session
        movies = session.query(Movie).join(MovieActor).filter(MovieActor.actor_id == actor_id).all()
        return movies

    def find_by_nationality(self, nationality_name: str) -> List[Actor]:
        return db.session.query(Actor).filter(Actor.nationality == nationality_name).all()
    
    def remove_actor_from_movie(self, movie_id: int, actor_id: int) -> None:
        db.session.query(MovieActor).filter(
            MovieActor.movie_id == movie_id,
            MovieActor.actor_id == actor_id
        ).delete()
        db.session.commit()

    def add_movie_to_actor(self, actor_id: int, movie_id: int, character_name: str, billing_order: Optional[int] = None) -> None:
        movie_actor = MovieActor(
            actor_id=actor_id,
            movie_id=movie_id,
            character_name=character_name,
            billing_order=billing_order
        )
        db.session.add(movie_actor)
        db.session.commit()
    
actor_dao = ActorDAO()