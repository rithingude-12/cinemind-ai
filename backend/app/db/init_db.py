from app.db.session import Base, engine
from app.models.user import User
from app.models.session import UserSession
from app.models.rating import Rating
from app.models.watchlist import Watchlist
from app.models.movie import Movie

def init_db():
    Base.metadata.create_all(bind=engine)
