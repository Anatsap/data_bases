from my_project import db
from my_project.auth.domain.i_dto import IDto
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class MovieGenre(db.Model):
    __tablename__ = 'movie_genres'
    
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.movie_id'), primary_key=True)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.genre_id'), primary_key=True)
    
    movie = db.relationship("Movie", back_populates="genres_link")
    genre = db.relationship("Genre", back_populates="movies_link")
    
    def __repr__(self):
        return f"MovieGenre(movie_id={self.movie_id}, genre_id={self.genre_id})"