

from typing import List
from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain.orders.movie import Movie
from t08_flask_mysql.app.my_project.auth.domain.orders.actor import Actor
from t08_flask_mysql.app.my_project.auth.domain.orders.movie_actor import MovieActor
import sqlalchemy

class MovieDAO(GeneralDAO):
    _domain_type = Movie
    def find_actors_by_movie_id(self, movie_id: int) -> List[Actor]:
        session = db.session
        actors = session.query(Actor).join(MovieActor).filter(MovieActor.movie_id == movie_id).all()
        return actors
    
    # def find_reviews_by_movie_id(self, movie_id: int):
    #     from t08_flask_mysql.app.my_project.auth.domain.orders.review import Review
    #     session = db.session
    #     reviews = session.query(Review).filter(Review.movie_id == movie_id).all()
    #     return reviews

    # def find_by_release_year(self, year: int) -> List[Movie]:
    #     return db.session.query(Movie).filter(Movie.release_year == year).all()
