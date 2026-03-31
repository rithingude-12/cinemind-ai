from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import or_, func
from typing import List, Optional
from app.db.session import get_db
from app.models.movie import Movie
from pydantic import BaseModel

router = APIRouter()

class MovieSearchResponse(BaseModel):
    id: int
    title: str
    poster_url: Optional[str] = None
    year: Optional[str] = None
    primary_genre: Optional[str] = None
    rating: Optional[float] = None

@router.get("/search", response_model=List[MovieSearchResponse])
def search_movies(
    q: str = Query(..., min_length=1, description="Search query"),
    limit: int = Query(10, le=50, description="Maximum number of results"),
    db: Session = Depends(get_db)
):
    """
    Search movies by title with case-insensitive matching.
    Returns top matching movies from the dataset.
    """
    if not q or len(q.strip()) < 1:
        return []
    
    # Case-insensitive search in movie titles
    search_query = q.strip().lower()
    
    movies = db.query(Movie).filter(
        or_(
            func.lower(Movie.title).contains(search_query),
            func.lower(Movie.original_title).contains(search_query)
        )
    ).limit(limit).all()
    
    # Convert to response format
    results = []
    for movie in movies:
        results.append(MovieSearchResponse(
            id=movie.id,
            title=movie.title,
            poster_url=movie.poster_url,
            year=str(movie.year) if movie.year else None,
            primary_genre=movie.primary_genre,
            rating=movie.rating
        ))
    
    return results

@router.get("/popular", response_model=List[MovieSearchResponse])
def get_popular_movies(
    limit: int = Query(20, le=100, description="Maximum number of results"),
    db: Session = Depends(get_db)
):
    """
    Get popular movies for manual mode suggestions.
    """
    movies = db.query(Movie).order_by(Movie.rating.desc()).limit(limit).all()
    
    results = []
    for movie in movies:
        results.append(MovieSearchResponse(
            id=movie.id,
            title=movie.title,
            poster_url=movie.poster_url,
            year=str(movie.year) if movie.year else None,
            primary_genre=movie.primary_genre,
            rating=movie.rating
        ))
    
    return results

@router.get("/{movie_id}", response_model=MovieSearchResponse)
def get_movie_by_id(
    movie_id: int,
    db: Session = Depends(get_db)
):
    """
    Get a specific movie by ID.
    """
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    
    if not movie:
        return None
    
    return MovieSearchResponse(
        id=movie.id,
        title=movie.title,
        poster_url=movie.poster_url,
        year=str(movie.year) if movie.year else None,
        primary_genre=movie.primary_genre,
        rating=movie.rating
    )
