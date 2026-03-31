import csv
import re
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.movie import Movie
from datetime import datetime

def parse_year_from_date(date_str):
    """Extract year from release_date string"""
    if not date_str or date_str == "":
        return None
    
    # Handle different date formats
    if "-" in date_str:
        # Format: "2005-03-27" or "2026-02-12"
        try:
            return int(date_str.split("-")[0])
        except (ValueError, IndexError):
            return None
    else:
        # Try to parse as just a year
        try:
            return int(date_str)
        except ValueError:
            return None

def parse_primary_genre(genre_str):
    """Extract primary genre from genre string"""
    if not genre_str or genre_str == "":
        return "Unknown"
    
    # Split by comma and take the first genre
    genres = [g.strip() for g in genre_str.split(",")]
    if genres:
        # Clean up genre names
        primary = genres[0]
        
        # Map common genre variations
        genre_mapping = {
            "Sci-Fi & Fantasy": "Science Fiction",
            "Science Fiction": "Science Fiction",
            "Action & Adventure": "Action",
            "Action": "Action",
            "Drama": "Drama",
            "Comedy": "Comedy",
            "Horror": "Horror",
            "Thriller": "Thriller",
            "Romance": "Romance",
            "Animation": "Animation",
            "Family": "Family",
            "Crime": "Crime",
            "Mystery": "Mystery",
            "Fantasy": "Fantasy",
            "Adventure": "Adventure",
            "War": "War",
            "Western": "Western",
            "Musical": "Musical",
            "Documentary": "Documentary",
            "Biography": "Biography",
            "History": "History",
            "Sport": "Sport",
            "Music": "Music",
            "Talk": "Talk",
            "Reality": "Reality",
            "Kids": "Family",
            "News": "News"
        }
        
        return genre_mapping.get(primary, primary)
    
    return "Unknown"

def clean_title(title):
    """Clean title by removing extra quotes and spaces"""
    if not title:
        return "Unknown Title"
    
    # Remove surrounding quotes if present
    title = title.strip()
    if title.startswith('"') and title.endswith('"'):
        title = title[1:-1]
    
    return title

def import_movies_from_csv():
    """
    Import all movies from the dataset CSV file.
    """
    db = SessionLocal()
    try:
        print("Starting import from movies.csv...")
        
        # Clear existing movies
        print("Clearing existing movies...")
        db.query(Movie).delete()
        db.commit()
        
        # Read CSV file
        csv_path = "c:/Users/RithinGude/Desktop/dataset/movies.csv"
        movies_added = 0
        movies_skipped = 0
        
        with open(csv_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            
            for row in csv_reader:
                try:
                    # Only process movies (skip TV series)
                    if row.get('type', '').lower() != 'movie':
                        movies_skipped += 1
                        continue
                    
                    # Extract and clean data
                    title = clean_title(row.get('title', ''))
                    original_title = clean_title(row.get('title', ''))
                    overview = row.get('overview', '')
                    poster_url = row.get('poster_url', '')
                    language = row.get('language', 'English')
                    year = parse_year_from_date(row.get('release_date', ''))
                    genre = parse_primary_genre(row.get('genre', ''))
                    
                    # Get rating (vote_average)
                    try:
                        rating = float(row.get('vote_average', 0.0))
                        if rating > 10:
                            rating = rating / 10  # Some datasets might have rating out of 100
                    except (ValueError, TypeError):
                        rating = 0.0
                    
                    # Skip if essential data is missing
                    if not title or title == "Unknown Title":
                        movies_skipped += 1
                        continue
                    
                    # Create movie object
                    movie = Movie(
                        title=title,
                        original_title=original_title,
                        overview=overview,
                        poster_url=poster_url,
                        backdrop_url="",  # Not in CSV
                        primary_genre=genre,
                        language=language,
                        year=year,
                        rating=rating,
                        runtime=None  # Not in CSV
                    )
                    
                    db.add(movie)
                    movies_added += 1
                    
                    # Commit in batches of 1000 to avoid memory issues
                    if movies_added % 1000 == 0:
                        db.commit()
                        print(f"Added {movies_added} movies...")
                
                except Exception as e:
                    print(f"Error processing row: {e}")
                    movies_skipped += 1
                    continue
        
        # Final commit
        db.commit()
        
        print(f"\nImport completed!")
        print(f"Movies added: {movies_added}")
        print(f"Movies skipped: {movies_skipped}")
        
        # Get final count
        final_count = db.query(Movie).count()
        print(f"Total movies in database: {final_count}")
        
    except Exception as e:
        print(f"Error during import: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    import_movies_from_csv()
