import requests
import json
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.movie import Movie
import time
from typing import List, Dict

def fetch_tmdb_movies(page: int = 1, total_pages: int = 1000) -> List[Dict]:
    """
    Fetch movies from TMDB API.
    Note: This requires a TMDB API key in a real implementation.
    For demo purposes, we'll create a comprehensive dataset.
    """
    # This would be the real TMDB API call with your API key
    # For now, we'll generate a comprehensive dataset
    movies = []
    
    # Sample comprehensive movie data - in reality this would be from TMDB API
    base_movies = [
        # Action/Adventure
        {"title": "The Dark Knight", "year": 2008, "genre": "Action", "rating": 9.0},
        {"title": "Avengers: Endgame", "year": 2019, "genre": "Action", "rating": 8.4},
        {"title": "Mission: Impossible - Fallout", "year": 2018, "genre": "Action", "rating": 7.7},
        {"title": "Mad Max: Fury Road", "year": 2015, "genre": "Action", "rating": 8.1},
        {"title": "John Wick", "year": 2014, "genre": "Action", "rating": 7.4},
        {"title": "Die Hard", "year": 1988, "genre": "Action", "rating": 8.2},
        {"title": "The Terminator", "year": 1984, "genre": "Action", "rating": 8.0},
        {"title": "Aliens", "year": 1986, "genre": "Action", "rating": 8.4},
        {"title": "Gladiator", "year": 2000, "genre": "Action", "rating": 8.5},
        {"title": "Braveheart", "year": 1995, "genre": "Action", "rating": 8.3},
        
        # Drama
        {"title": "The Shawshank Redemption", "year": 1994, "genre": "Drama", "rating": 9.3},
        {"title": "The Godfather", "year": 1972, "genre": "Drama", "rating": 9.2},
        {"title": "The Godfather: Part II", "year": 1974, "genre": "Drama", "rating": 9.0},
        {"title": "Schindler's List", "year": 1993, "genre": "Drama", "rating": 9.0},
        {"title": "12 Angry Men", "year": 1957, "genre": "Drama", "rating": 9.0},
        {"title": "Forrest Gump", "year": 1994, "genre": "Drama", "rating": 8.8},
        {"title": "Fight Club", "year": 1999, "genre": "Drama", "rating": 8.8},
        {"title": "The Green Mile", "year": 1999, "genre": "Drama", "rating": 8.6},
        {"title": "Goodfellas", "year": 1990, "genre": "Drama", "rating": 8.7},
        {"title": "The Departed", "year": 2006, "genre": "Drama", "rating": 8.5},
        
        # Sci-Fi
        {"title": "Inception", "year": 2010, "genre": "Science Fiction", "rating": 8.8},
        {"title": "The Matrix", "year": 1999, "genre": "Science Fiction", "rating": 8.7},
        {"title": "Interstellar", "year": 2014, "genre": "Science Fiction", "rating": 8.6},
        {"title": "Star Wars: A New Hope", "year": 1977, "genre": "Science Fiction", "rating": 8.6},
        {"title": "Blade Runner 2049", "year": 2017, "genre": "Science Fiction", "rating": 8.0},
        {"title": "2001: A Space Odyssey", "year": 1968, "genre": "Science Fiction", "rating": 8.3},
        {"title": "Alien", "year": 1979, "genre": "Science Fiction", "rating": 8.4},
        {"title": "The Empire Strikes Back", "year": 1980, "genre": "Science Fiction", "rating": 8.7},
        {"title": "Return of the Jedi", "year": 1983, "genre": "Science Fiction", "rating": 8.3},
        {"title": "Blade Runner", "year": 1982, "genre": "Science Fiction", "rating": 8.1},
    ]
    
    # Generate variations to create a large dataset
    for base in base_movies:
        movies.append({
            "id": len(movies) + 1,
            "title": base["title"],
            "original_title": base["title"],
            "overview": f"Overview for {base['title']}",
            "poster_url": f"https://image.tmdb.org/t/p/w500/{base['title'].replace(' ', '').lower()}.jpg",
            "backdrop_url": f"https://image.tmdb.org/t/p/w500/{base['title'].replace(' ', '').lower()}_backdrop.jpg",
            "primary_genre": base["genre"],
            "language": "English",
            "year": base["year"],
            "rating": base["rating"],
            "runtime": 120
        })
    
    return movies

def generate_comprehensive_dataset() -> List[Dict]:
    """
    Generate a comprehensive dataset of 35,000 movies.
    This creates realistic movie data across all genres and decades.
    """
    
    # Base movie templates
    titles = [
        "The", "A", "My", "Life", "Love", "Death", "Night", "Day", "Dream", "Story",
        "Journey", "Adventure", "Mystery", "Secret", "Hidden", "Lost", "Found", "Return",
        "Escape", "Chase", "Hunt", "Search", "Discovery", "Beginning", "End", "War", "Peace",
        "Hope", "Despair", "Joy", "Sorrow", "Victory", "Defeat", "Rise", "Fall", "Rebirth"
    ]
    
    adjectives = [
        "Dark", "Light", "Silent", "Loud", "Fast", "Slow", "Big", "Small", "Old", "New",
        "Red", "Blue", "Green", "Golden", "Silver", "Black", "White", "Cold", "Hot", "Wild",
        "Tame", "Brave", "Cowardly", "Strong", "Weak", "Smart", "Dumb", "Rich", "Poor",
        "Happy", "Sad", "Angry", "Calm", "Crazy", "Normal", "Strange", "Magic", "Real"
    ]
    
    nouns = [
        "Knight", "Princess", "King", "Queen", "Dragon", "Castle", "Forest", "Ocean", "Mountain",
        "River", "City", "Town", "Village", "House", "Home", "School", "Church", "Temple",
        "Garden", "Park", "Street", "Road", "Bridge", "Gate", "Door", "Window", "Room",
        "Book", "Letter", "Message", "Secret", "Mystery", "Crime", "Murder", "Theft", "Love",
        "Hate", "Fear", "Hope", "Dream", "Nightmare", "Reality", "Fantasy", "World", "Universe"
    ]
    
    genres = [
        "Action", "Adventure", "Comedy", "Drama", "Fantasy", "Horror", "Mystery", "Romance",
        "Science Fiction", "Thriller", "Crime", "Animation", "Family", "War", "Western", "Musical",
        "Documentary", "Biography", "History", "Sport", "Music", "Film Noir", "TV Movie"
    ]
    
    languages = ["English", "Spanish", "French", "German", "Italian", "Japanese", "Chinese", "Korean", "Russian", "Hindi"]
    
    movies = []
    movie_id = 1
    
    # Generate 35,000 movies
    for i in range(35000):
        # Create realistic movie titles
        if i % 4 == 0:
            title = f"{titles[i % len(titles)]} {adjectives[i % len(adjectives)]} {nouns[i % len(nouns)]}"
        elif i % 4 == 1:
            title = f"{adjectives[i % len(adjectives)]} {nouns[i % len(nouns)]}"
        elif i % 4 == 2:
            title = f"{nouns[i % len(nouns)]} of the {titles[i % len(titles)]}"
        else:
            title = f"{titles[i % len(titles)]} {nouns[i % len(nouns)]}"
        
        # Vary years from 1920 to 2024
        year = 1920 + (i % 105)
        
        # Assign genre based on some pattern
        genre = genres[i % len(genres)]
        
        # Vary ratings realistically
        rating = 5.0 + (i % 50) / 10.0  # Ratings from 5.0 to 9.9
        
        # Create movie data (without ID - let database auto-generate)
        movie_data = {
            "title": title,
            "original_title": title,
            "overview": f"A compelling story about {title.lower()}, featuring drama, action, and unforgettable characters. Set in {year}, this film explores themes of love, loss, and redemption.",
            "poster_url": f"https://image.tmdb.org/t/p/w500/poster_{movie_id}.jpg",
            "backdrop_url": f"https://image.tmdb.org/t/p/w500/backdrop_{movie_id}.jpg",
            "primary_genre": genre,
            "language": languages[i % len(languages)],
            "year": year,
            "rating": round(rating, 1),
            "runtime": 80 + (i % 120)  # Runtime from 80 to 200 minutes
        }
        
        movies.append(movie_data)
        movie_id += 1
        
        # Progress indicator
        if i % 1000 == 0:
            print(f"Generated {i} movies...")
    
    return movies

def add_massive_movie_dataset():
    """
    Add 35,000 movies to the database.
    """
    db = SessionLocal()
    try:
        print("Starting massive movie dataset import...")
        
        # Check existing count
        existing_count = db.query(Movie).count()
        print(f"Current movie count: {existing_count}")
        
        # Generate comprehensive dataset
        print("Generating 35,000 movies...")
        movies = generate_comprehensive_dataset()
        
        print(f"Generated {len(movies)} movies. Adding to database...")
        
        # Add movies in batches to avoid memory issues
        batch_size = 1000
        added_count = 0
        
        for i in range(0, len(movies), batch_size):
            batch = movies[i:i + batch_size]
            
            for movie_data in batch:
                # Check if movie already exists
                existing = db.query(Movie).filter(Movie.title == movie_data["title"]).first()
                if not existing:
                    movie = Movie(**movie_data)
                    db.add(movie)
                    added_count += 1
            
            # Commit batch
            db.commit()
            print(f"Added batch {i//batch_size + 1}/{(len(movies)//batch_size) + 1} (Total added: {added_count})")
        
        final_count = db.query(Movie).count()
        print(f"Successfully added {added_count} new movies")
        print(f"Total movies in database: {final_count}")
        
    except Exception as e:
        print(f"Error adding massive dataset: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_massive_movie_dataset()
