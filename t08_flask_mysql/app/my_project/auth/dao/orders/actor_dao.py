"""
©2022-2023 Andrii Pavelchak, apavelchak@gmail.com
Realisation of Actor data access layer.
"""

from typing import List
from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain.orders.actor import Actor
from t08_flask_mysql.app.my_project.auth.domain.orders.movie_actor import MovieActor
from t08_flask_mysql.app.my_project.auth.domain.orders.movie import Movie
import sqlalchemy

class ActorDAO(GeneralDAO):
    _domain_type = Actor
    def find_movies_by_actor_id(self, actor_id: int) -> List[Movie]:
        session = db.session
        movies = session.query(Movie).join(MovieActor).filter(MovieActor.actor_id == actor_id).all()
        return movies
    

    def find_by_nationality(self, nationality_name: str) -> List[Actor]:
        return db.session.query(Actor).filter(Actor.nationality == nationality_name).all()