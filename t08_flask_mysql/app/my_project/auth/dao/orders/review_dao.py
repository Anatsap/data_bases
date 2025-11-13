
from typing import List
from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain.orders.review import Review

class ReviewDAO(GeneralDAO):
    _domain_type = Review
    def find_reviews_by_movie_id(self, movie_id: int) -> List[Review]:
        session = db.session
        return session.query(Review).filter(Review.movie_id == movie_id).all()