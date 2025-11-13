from .movie_service import MovieService
from .country_service import CountryService
from .actor_service import ActorService
from .review_service import ReviewService
from .genre_service import GenreService


movie_service = MovieService()
country_service = CountryService()
actor_service = ActorService()
review_service = ReviewService()
genre_service = GenreService()