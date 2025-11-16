"""
2023
apavelchak@gmail.com
© Andrii Pavelchak
"""

from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    from .orders.movie_route import movie_bp
    from .orders.actor_route import actor_bp
    from .orders.review_route import review_bp
    from .orders.country_route import country_bp
    from .orders.genre_route import genre_bp

    app.register_blueprint(movie_bp)
    app.register_blueprint(actor_bp)
    app.register_blueprint(review_bp)
    app.register_blueprint(country_bp)
    app.register_blueprint(genre_bp)


