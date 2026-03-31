from sqlalchemy import Column, Integer, String, Float, Text
from app.db.session import Base

class Movie(Base):
    __tablename__ = "movies"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    original_title = Column(String, nullable=True)
    overview = Column(Text, nullable=True)
    poster_url = Column(String, nullable=True)
    backdrop_url = Column(String, nullable=True)
    primary_genre = Column(String, nullable=True, index=True)
    language = Column(String, nullable=True, index=True)
    year = Column(Integer, nullable=True, index=True)
    rating = Column(Float, nullable=True, index=True)
    runtime = Column(Integer, nullable=True)
    
    def __repr__(self):
        return f"<Movie(id={self.id}, title='{self.title}', year={self.year})>"
