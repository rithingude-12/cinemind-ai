from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import or_, and_, func
from typing import List, Optional
from app.db.session import get_db
from app.core.dependencies import get_current_user
from app.models.user import User
from app.models.movie import Movie
from pydantic import BaseModel

router = APIRouter()

class QuestionnaireRequest(BaseModel):
    user_id: Optional[str] = None
    language: str
    era: str
    genres: List[str]

class ManualRequest(BaseModel):
    user_id: Optional[str] = None
    language: str
    era: str
    movie_ids: List[int]

class RecommendationResponse(BaseModel):
    hero: Optional[dict] = None
    primary: List[dict] = []
    extended: List[dict] = []
    explanation: str
    confidence_score: float

def movie_to_dict(movie: Movie) -> dict:
    """Convert movie object to dictionary format"""
    return {
        "id": movie.id,
        "title": movie.title,
        "year": str(movie.year) if movie.year else None,
        "poster_url": movie.poster_url,
        "primary_genre": movie.primary_genre,
        "rating": movie.rating,
        "overview": movie.overview or "",
        "language": movie.language or "English"
    }

@router.post("/questionnaire", response_model=RecommendationResponse)
def questionnaire_recommendations(request: QuestionnaireRequest, db: Session = Depends(get_db)):
    """
    Generate recommendations based on selected genres.
    """
    # Build query for genre-based filtering
    genre_conditions = []
    for genre in request.genres:
        genre_conditions.append(func.lower(Movie.primary_genre) == genre.lower())
    
    # Filter by language and era if specified
    query = db.query(Movie)
    
    if request.language and request.language != "All":
        query = query.filter(func.lower(Movie.language) == request.language.lower())
    
    if request.era and request.era != "All":
        # Map era to year ranges
        era_map = {
            "2020s": (2020, 2029),
            "2010s": (2010, 2019),
            "2000s": (2000, 2009),
            "1990s": (1990, 1999),
            "1980s": (1980, 1989),
            "1970s": (1970, 1979)
        }
        if request.era in era_map:
            start_year, end_year = era_map[request.era]
            query = query.filter(and_(Movie.year >= start_year, Movie.year <= end_year))
    
    # Apply genre filters
    if genre_conditions:
        query = query.filter(or_(*genre_conditions))
    
    # Get movies and sort by rating
    movies = query.order_by(Movie.rating.desc()).limit(50).all()
    
    # Convert to response format
    movie_dicts = [movie_to_dict(movie) for movie in movies]
    
    if len(movie_dicts) == 0:
        return RecommendationResponse(
            hero=None,
            primary=[],
            extended=[],
            explanation=f"No movies found for {', '.join(request.genres)} genres.",
            confidence_score=0.0
        )
    
    # Structure response
    hero = movie_dicts[0]
    primary = movie_dicts[1:8] if len(movie_dicts) > 1 else []
    extended = movie_dicts[8:30] if len(movie_dicts) > 8 else movie_dicts[1:30]
    
    return RecommendationResponse(
        hero=hero,
        primary=primary,
        extended=extended,
        explanation=f"Because you selected {', '.join(request.genres)} genres, we found these movies that match your taste perfectly.",
        confidence_score=92.0
    )

@router.post("/manual", response_model=RecommendationResponse)
def manual_recommendations(request: ManualRequest, db: Session = Depends(get_db)):
    """
    Generate recommendations based on selected movies using similarity.
    """
    # Get the selected movies
    selected_movies = db.query(Movie).filter(Movie.id.in_(request.movie_ids)).all()
    
    if len(selected_movies) < 3:
        return RecommendationResponse(
            hero=None,
            primary=[],
            extended=[],
            explanation="Please select exactly 3 movies for analysis.",
            confidence_score=0.0
        )
    
    # Extract genres from selected movies
    selected_genres = set()
    for movie in selected_movies:
        if movie.primary_genre:
            selected_genres.add(movie.primary_genre.lower())
    
    # Find similar movies based on genres
    genre_conditions = []
    for genre in selected_genres:
        genre_conditions.append(func.lower(Movie.primary_genre) == genre)
    
    # Filter by language and era
    query = db.query(Movie).filter(~Movie.id.in_(request.movie_ids))
    
    if request.language and request.language != "All":
        query = query.filter(func.lower(Movie.language) == request.language.lower())
    
    if request.era and request.era != "All":
        era_map = {
            "2020s": (2020, 2029),
            "2010s": (2010, 2019),
            "2000s": (2000, 2009),
            "1990s": (1990, 1999),
            "1980s": (1980, 1989),
            "1970s": (1970, 1979)
        }
        if request.era in era_map:
            start_year, end_year = era_map[request.era]
            query = query.filter(and_(Movie.year >= start_year, Movie.year <= end_year))
    
    # Apply genre similarity filters
    if genre_conditions:
        query = query.filter(or_(*genre_conditions))
    
    # Get similar movies and sort by rating
    similar_movies = query.order_by(Movie.rating.desc()).limit(50).all()
    
    # Convert to response format
    movie_dicts = [movie_to_dict(movie) for movie in similar_movies]
    
    if len(movie_dicts) == 0:
        return RecommendationResponse(
            hero=None,
            primary=[],
            extended=[],
            explanation="No similar movies found in our database.",
            confidence_score=0.0
        )
    
    # Structure response
    hero = movie_dicts[0]
    primary = movie_dicts[1:8] if len(movie_dicts) > 1 else []
    extended = movie_dicts[8:30] if len(movie_dicts) > 8 else movie_dicts[1:30]
    
    selected_titles = [movie.title for movie in selected_movies]
    
    return RecommendationResponse(
        hero=hero,
        primary=primary,
        extended=extended,
        explanation=f"Because you loved {', '.join(selected_titles)}, we found similar films that match your sophisticated taste.",
        confidence_score=89.0
    )
