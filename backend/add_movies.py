from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.movie import Movie

def add_sample_movies():
    db = SessionLocal()
    try:
        # Check if movies already exist
        existing_movies = db.query(Movie).count()
        if existing_movies > 0:
            print(f"Database already has {existing_movies} movies")
            return
        
        # Sample movie data
        sample_movies = [
            {
                "title": "The Dark Knight",
                "original_title": "The Dark Knight",
                "overview": "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham Batman must accept one of the greatest psychological and physical tests.",
                "poster_url": "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haID0jeZ.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/6odIwC1gvcB9c5VhIYj8Bp3aT7b.jpg",
                "primary_genre": "Action",
                "language": "English",
                "year": 2008,
                "rating": 9.0,
                "runtime": 152
            },
            {
                "title": "Inception",
                "original_title": "Inception",
                "overview": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.",
                "poster_url": "https://image.tmdb.org/t/p/w500/9gk7adLYIbdfzd2Ypt4TVYPWZ9E.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/s3TBrRGB1iav7gFoKp3MxcKsLyKS.jpg",
                "primary_genre": "Science Fiction",
                "language": "English",
                "year": 2010,
                "rating": 8.8,
                "runtime": 148
            },
            {
                "title": "The Matrix",
                "original_title": "The Matrix",
                "overview": "A computer programmer discovers that reality as he knows it is a simulation created by machines, and joins a rebellion to break free.",
                "poster_url": "https://image.tmdb.org/t/p/w500/fiU72sd6R7iH6jULbSyEhDaOcSa.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/AuKiKK0Sg0571yHYZB1QrfgUml9.jpg",
                "primary_genre": "Science Fiction",
                "language": "English",
                "year": 1999,
                "rating": 8.7,
                "runtime": 136
            },
            {
                "title": "Pulp Fiction",
                "original_title": "Pulp Fiction",
                "overview": "The lives of two mob hitmen, a boxer, a gangster and his wife intertwine in four tales of violence and redemption.",
                "poster_url": "https://image.tmdb.org/t/p/w500/plnlrtBUVXAhM5N5rjFba2Z6v9V.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/pdFc12g3NJcHhcH4gza4JhxI5hy.jpg",
                "primary_genre": "Crime",
                "language": "English",
                "year": 1994,
                "rating": 8.9,
                "runtime": 154
            },
            {
                "title": "The Shawshank Redemption",
                "original_title": "The Shawshank Redemption",
                "overview": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5KCVkauXWt5UeC1Uxw9BHWf2dPd.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/6uCddVD6ccNjP5uc4zv7UA8PjxQ.jpg",
                "primary_genre": "Drama",
                "language": "English",
                "year": 1994,
                "rating": 9.3,
                "runtime": 142
            },
            {
                "title": "Fight Club",
                "original_title": "Fight Club",
                "overview": "An insomniac office worker and a devil-may-care soap maker form an underground fight club that evolves into much more.",
                "poster_url": "https://image.tmdb.org/t/p/w500/pB8BM7pdSp6B6Ih7QZ4DrQ3PmJK.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/fCayJrkfRaCRCTh8GqN30f8oyQF.jpg",
                "primary_genre": "Drama",
                "language": "English",
                "year": 1999,
                "rating": 8.8,
                "runtime": 139
            },
            {
                "title": "Forrest Gump",
                "original_title": "Forrest Gump",
                "overview": "The presidencies of Kennedy and Johnson, the Vietnam War, the Watergate scandal and other historical events unfold from the perspective of an Alabama man.",
                "poster_url": "https://image.tmdb.org/t/p/w500/saHP97ECOiXmgdVCONCqF2ntkJA.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/8QPGs5LhXxfD7ObglHr3QajH9Tf.jpg",
                "primary_genre": "Drama",
                "language": "English",
                "year": 1994,
                "rating": 8.8,
                "runtime": 142
            },
            {
                "title": "Interstellar",
                "original_title": "Interstellar",
                "overview": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
                "poster_url": "https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/rAiYTfKGqDC1I2iWw9Mvrr1GOaS.jpg",
                "primary_genre": "Science Fiction",
                "language": "English",
                "year": 2014,
                "rating": 8.6,
                "runtime": 169
            },
            {
                "title": "The Godfather",
                "original_title": "The Godfather",
                "overview": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
                "poster_url": "https://image.tmdb.org/t/p/w500/3bhkrj58Vtu7enYsRolD1fZbjae.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/rqAeRtUL89kNnYdZs9BJJwMikEJ.jpg",
                "primary_genre": "Crime",
                "language": "English",
                "year": 1972,
                "rating": 9.2,
                "runtime": 175
            },
            {
                "title": "Goodfellas",
                "original_title": "Goodfellas",
                "overview": "The story of Henry Hill and his life in the mob, covering his relationship with his wife Karen Hill and his mob partners.",
                "poster_url": "https://image.tmdb.org/t/p/w500/aKuFiU82s5iNBZyErgDuA1A02rI.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/vI6dVtT2w9GtMNO2d5hVcL2K3q2.jpg",
                "primary_genre": "Crime",
                "language": "English",
                "year": 1990,
                "rating": 8.7,
                "runtime": 146
            },
            {
                "title": "The Prestige",
                "original_title": "The Prestige",
                "overview": "After a tragic accident, two stage magicians engage in a battle to create the ultimate illusion while sacrificing everything they have to outwit each other.",
                "poster_url": "https://image.tmdb.org/t/p/w500/8rbT5VxvNqLk1JjPmxiBIAvQg4v.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/6vKqAGKcKb3mVtA5RkIwiy3nT3J.jpg",
                "primary_genre": "Mystery",
                "language": "English",
                "year": 2006,
                "rating": 8.5,
                "runtime": 130
            },
            {
                "title": "Django Unchained",
                "original_title": "Django Unchained",
                "overview": "With the help of a German bounty-hunter, a freed slave sets out to rescue his wife from a brutal plantation-owner in Mississippi.",
                "poster_url": "https://image.tmdb.org/t/p/w500/7oW32chc9wVjlnb4ozpWOOvDhJ8.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/eIEk2MKvKlCO2xvKoaCVgB9pWmX.jpg",
                "primary_genre": "Drama",
                "language": "English",
                "year": 2012,
                "rating": 8.4,
                "runtime": 165
            },
            {
                "title": "The Departed",
                "original_title": "The Departed",
                "overview": "An undercover cop and a mole in the police attempt to identify each other while infiltrating an Irish gang in South Boston.",
                "poster_url": "https://image.tmdb.org/t/p/w500/3h1UZBqJlHLZBnJcA5OQfjYktI9.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/crsXZTrRPHcZ8WACbVCKUK7v.jpg",
                "primary_genre": "Crime",
                "language": "English",
                "year": 2006,
                "rating": 8.5,
                "runtime": 151
            },
            {
                "title": "Shutter Island",
                "original_title": "Shutter Island",
                "overview": "A U.S. Marshal investigates the disappearance of a murderer who escaped from a hospital for the criminally insane.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5LJGrwtVZ6v6u7dVb2Bm9I2H6QD.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/9LgK8j5b5Z9FZJzZ8ZjZ9ZJzZ9Z.jpg",
                "primary_genre": "Thriller",
                "language": "English",
                "year": 2010,
                "rating": 8.2,
                "runtime": 138
            },
            {
                "title": "Mad Max: Fury Road",
                "original_title": "Mad Max: Fury Road",
                "overview": "In a post-apocalyptic wasteland, a woman rebels against a tyrannical ruler in search for her homeland with the aid of a group of female prisoners.",
                "poster_url": "https://image.tmdb.org/t/p/w500/8zUbPeAMrnCilxA9IlFj2XrVsL.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/4kHlEWxL9Z6J6J6J6J6J6J6J6J6.jpg",
                "primary_genre": "Action",
                "language": "English",
                "year": 2015,
                "rating": 8.1,
                "runtime": 120
            },
            {
                "title": "Blade Runner 2049",
                "original_title": "Blade Runner 2049",
                "overview": "A young blade runner's discovery of a long-buried secret leads him to track down former blade runner Rick Deckard.",
                "poster_url": "https://image.tmdb.org/t/p/w500/gCcnJlHc9VvJ4hXJq7I8J9J9J9J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5gEJNn5J5J5J5J5J5J5J5J5J5J.jpg",
                "primary_genre": "Science Fiction",
                "language": "English",
                "year": 2017,
                "rating": 8.0,
                "runtime": 164
            },
            {
                "title": "John Wick",
                "original_title": "John Wick",
                "overview": "An ex-hitman comes out of retirement to track down the gangsters that killed his dog and stole his car.",
                "poster_url": "https://image.tmdb.org/t/p/w500/j9dJk8lJk8lJk8lJk8lJk8lJk8l.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/kJk8lJk8lJk8lJk8lJk8lJk8lJ.jpg",
                "primary_genre": "Action",
                "language": "English",
                "year": 2014,
                "rating": 7.4,
                "runtime": 101
            },
            {
                "title": "Edge of Tomorrow",
                "original_title": "Edge of Tomorrow",
                "overview": "A soldier fighting aliens gets to relive the same day over and over again, each time getting better at fighting.",
                "poster_url": "https://image.tmdb.org/t/p/w500/Jk8lJk8lJk8lJk8lJk8lJk8lJk8.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/lJk8lJk8lJk8lJk8lJk8lJk8lJ.jpg",
                "primary_genre": "Science Fiction",
                "language": "English",
                "year": 2014,
                "rating": 7.9,
                "runtime": 113
            }
        ]
        
        # Add movies to database
        for movie_data in sample_movies:
            movie = Movie(**movie_data)
            db.add(movie)
        
        db.commit()
        print(f"Added {len(sample_movies)} sample movies to database")
        
    except Exception as e:
        print(f"Error adding sample movies: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_sample_movies()
