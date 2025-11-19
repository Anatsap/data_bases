
from my_project import db
from my_project.auth.domain.i_dto import IDto
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

class MovieActor(db.Model):
    __tablename__ = 'movie_actors'
    
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.movie_id'), primary_key=True)
    actor_id = db.Column(db.Integer, db.ForeignKey('actors.actor_id'), primary_key=True)
    character_name = db.Column(db.String(60))
    billing_order = db.Column(db.Integer)
    
    movie = db.relationship("Movie", back_populates="actor")
    actor = db.relationship("Actor", back_populates="movie")

    def __repr__(self):
        return f"MovieActor(movie_id={self.movie_id}, actor_id={self.actor_id})"