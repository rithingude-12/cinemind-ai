from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.dependencies import get_current_user
from app.schemas.recommend import RecommendRequest, RecommendationResponse
from app.services.recommendation_engine import engine_instance
from app.models.user import User

router = APIRouter()

@router.post("/", response_model=RecommendationResponse)
def get_recommendations(request: RecommendRequest, db: Session = Depends(get_db)):
    # You can also use dependencies: `current_user: User = Depends(get_current_user)`
    res = engine_instance.get_recommendations(request)
    return res
