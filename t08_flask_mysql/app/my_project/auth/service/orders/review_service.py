
from typing import List, Dict, Any, Optional
from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao.orders.review_dao import review_dao
from my_project.auth.domain.orders.review import Review
from my_project.auth.domain.orders.movie import Movie


class ReviewService(GeneralService):
    _dao = review_dao  

    def find_movie_by_review_id(self, review_id: int) -> Optional[Dict[str, Any]]:
        movie_review: Optional[Movie] = self._dao.find_movie_by_review_id(review_id)
        if movie_review:
            return movie_review.put_into_dto()
        return None

    def delete(self, review_id: int) -> None:
        self._dao.delete(review_id)

review_service = ReviewService()
