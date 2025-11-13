"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""


from .movie_dao import MovieDAO
from .actor_dao import ActorDAO
from .country_dao import CountryDAO
from .review_dao import ReviewDAO
from .genre_dao import GenreDAO 

movie_dao = MovieDAO()
actor_dao = ActorDAO()
country_dao = CountryDAO()
review_dao = ReviewDAO()
genre_dao = GenreDAO()