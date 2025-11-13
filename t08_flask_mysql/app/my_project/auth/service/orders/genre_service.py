

from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService
from t08_flask_mysql.app.my_project.auth.dao.orders import genre_dao
from t08_flask_mysql.app.my_project.auth.domain.orders.genre import Genre

class GenreService(GeneralService):
    _dao = genre_dao