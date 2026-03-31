from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.dependencies import get_current_user
from app.models.rating import Rating
from app.models.user import User
from pydantic import BaseModel

class RatingCreate(BaseModel):
    movie_id: int
    rating: float

router = APIRouter()

@router.post("/")
def add_rating(request: RatingCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    existing = db.query(Rating).filter(Rating.user_id == current_user.id, Rating.movie_id == request.movie_id).first()
    if existing:
        existing.rating = request.rating
    else:
        new_rating = Rating(user_id=current_user.id, movie_id=request.movie_id, rating=request.rating)
        db.add(new_rating)
    db.commit()
    return {"message": "Rating saved successfully"}
