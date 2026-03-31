from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.dependencies import get_current_user
from app.models.watchlist import Watchlist
from app.models.user import User

router = APIRouter()

@router.get("/")
def get_watchlist(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    items = db.query(Watchlist).filter(Watchlist.user_id == current_user.id).all()
    return {"watchlist": [i.movie_id for i in items]}

@router.post("/add")
def add_to_watchlist(movie_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    existing = db.query(Watchlist).filter(Watchlist.user_id == current_user.id, Watchlist.movie_id == movie_id).first()
    if existing:
        return {"message": "Already in watchlist"}
    item = Watchlist(user_id=current_user.id, movie_id=movie_id)
    db.add(item)
    db.commit()
    return {"message": "Added to watchlist"}

@router.delete("/remove")
def remove_from_watchlist(movie_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    item = db.query(Watchlist).filter(Watchlist.user_id == current_user.id, Watchlist.movie_id == movie_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Not found in watchlist")
    db.delete(item)
    db.commit()
    return {"message": "Removed from watchlist"}
