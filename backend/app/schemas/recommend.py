from pydantic import BaseModel
from typing import List, Optional

class RecommendRequest(BaseModel):
    user_id: Optional[int] = None
    language: str
    era: str
    mode: str # 'mood', 'questionnaire', 'manual'
    mood: Optional[str] = None # 'dark', 'happy', 'balanced'
    energy: Optional[str] = None # 'low', 'high'
    questionnaire_genres: Optional[List[str]] = None
    manual_movies: Optional[List[int]] = None # list of movie ids

class MovieResponse(BaseModel):
    id: int
    title: str
    genres: List[str]
    primary_genre: str
    language: str
    year: int
    era: str
    rating: float
    popularity: float
    overview: str
    keywords: List[str]
    poster_url: str

class RecommendationResponse(BaseModel):
    movies: List[MovieResponse]
    explanation: str
    confidence_score: float
