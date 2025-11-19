
from typing import List, Optional
from my_project import db
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.review import Review
from my_project.auth.domain.orders.movie import Movie


class ReviewDAO(GeneralDAO):
    _domain_type = Review
    
    def find_movie_by_review_id(self, review_id: int) -> Optional[Movie]:
        session = db.session
        review_obj = session.query(Review).filter(Review.review_id == review_id).one_or_none()
        
        if review_obj and review_obj.movie_id:
            movie = session.query(Movie).filter(Movie.movie_id == review_obj.movie_id).one_or_none()
            return movie
        
        return None
    
review_dao = ReviewDAO()