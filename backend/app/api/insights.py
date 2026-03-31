from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.dependencies import get_current_user
from app.models.user import User
from app.models.rating import Rating
from app.models.watchlist import Watchlist
from app.services.recommendation_engine import engine_instance
import pandas as pd

router = APIRouter()

@router.get("/user")
def get_user_insights(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # 1. Fetch interactions
    ratings = db.query(Rating).filter(Rating.user_id == current_user.id).all()
    watchlist = db.query(Watchlist).filter(Watchlist.user_id == current_user.id).all()
    
    rated_ids = [r.movie_id for r in ratings]
    watchlist_ids = [w.movie_id for w in watchlist]
    all_ids = list(set(rated_ids + watchlist_ids))
    
    if not all_ids:
        return {
            "favorite_genres": [],
            "language_distribution": [],
            "era_distribution": [],
            "avg_rating": 0.0,
            "total_interactions": 0,
            "timeline": []
        }
    
    # 2. Filter dataset for these movies
    df_user = engine_instance.df[engine_instance.df['id'].isin(all_ids)].copy()
    
    # 3. Simple aggregations
    genre_counts = df_user['primary_genre'].value_counts().head(5).to_dict()
    lang_counts = df_user['language'].value_counts().to_dict()
    era_counts = df_user['era'].value_counts().to_dict()
    
    # 4. Timeline (Taste Shifts)
    # Simulate based on genre shifts in recent ratings
    timeline = [
        {
            "id": 1,
            "type": "mood_shift",
            "title": f"Shifted toward {df_user['primary_genre'].iloc[0] if not df_user.empty else 'new genres'}",
            "description": "Your recent interactions show an increasing preference for this category.",
            "movies": [
                {
                    "title": row['title'],
                    "poster_url": row['poster_url'],
                    "year": row['year']
                } for _, row in df_user.head(3).iterrows()
            ]
        }
    ]
    
    return {
        "favorite_genres": [{"genre": k, "count": int(v)} for k, v in genre_counts.items()],
        "language_distribution": [{"language": k, "count": int(v)} for k, v in lang_counts.items()],
        "era_distribution": [{"era": k, "count": int(v)} for k, v in era_counts.items()],
        "avg_rating": round(float(sum([r.rating for r in ratings]) / len(ratings)), 1) if ratings else 0.0,
        "total_interactions": len(all_ids),
        "timeline": timeline
    }

@router.get("/global")
def get_global_insights():
    # Performance aggregation on the full 30k dataset
    df = engine_instance.df
    
    genre_counts = df['primary_genre'].value_counts().head(8).to_dict()
    lang_counts = df['language'].value_counts().to_dict()
    era_counts = df['era'].value_counts().to_dict()
    
    return {
        "genres": [{"genre": k, "count": int(v)} for k, v in genre_counts.items()],
        "languages": [{"language": k, "count": int(v)} for k, v in lang_counts.items()],
        "eras": [{"era": k, "count": int(v)} for k, v in era_counts.items()]
    }
