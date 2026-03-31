from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.movie import Movie

def clear_and_add_massive_dataset():
    """
    Clear existing movies and add 35,000 new ones.
    """
    db = SessionLocal()
    try:
        print("Clearing existing movies...")
        db.query(Movie).delete()
        db.commit()
        
        print("Generating 35,000 movies...")
        
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
        
        movies_added = 0
        batch_size = 500  # Smaller batches for stability
        
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
            
            # Create movie data
            movie = Movie(
                title=title,
                original_title=title,
                overview=f"A compelling story about {title.lower()}, featuring drama, action, and unforgettable characters. Set in {year}, this film explores themes of love, loss, and redemption.",
                poster_url=f"https://image.tmdb.org/t/p/w500/poster_{i+1}.jpg",
                backdrop_url=f"https://image.tmdb.org/t/p/w500/backdrop_{i+1}.jpg",
                primary_genre=genre,
                language=languages[i % len(languages)],
                year=year,
                rating=round(rating, 1),
                runtime=80 + (i % 120)  # Runtime from 80 to 200 minutes
            )
            
            db.add(movie)
            movies_added += 1
            
            # Commit in batches
            if movies_added % batch_size == 0:
                db.commit()
                print(f"Added {movies_added} movies...")
        
        # Final commit
        db.commit()
        
        final_count = db.query(Movie).count()
        print(f"Successfully added {movies_added} movies to database!")
        print(f"Total movies in database: {final_count}")
        
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    clear_and_add_massive_dataset()
