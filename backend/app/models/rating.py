from sqlalchemy import Column, Integer, Float, ForeignKey
from app.db.session import Base

class Rating(Base):
    __tablename__ = "ratings"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    movie_id = Column(Integer, index=True)
    rating = Column(Float, nullable=False)
