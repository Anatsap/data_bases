from t08_flask_mysql.app.my_project import db
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

class MovieDirector(db.Model):
    __tablename__ = 'movie_directors'
    
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.movie_id'), primary_key=True)
    director_id = db.Column(db.Integer, db.ForeignKey('directors.director_id'), primary_key=True)
    
    movie = relationship("Movie", back_populates="directors_link")
    director = relationship("Director", back_populates="movies_link")
    
    def __repr__(self):
        return f"MovieDirector(movie_id={self.movie_id}, director_id={self.director_id})"