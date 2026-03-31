from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.movie import Movie

def add_comprehensive_movies():
    db = SessionLocal()
    try:
        # Check existing movies
        existing_movies = db.query(Movie).count()
        print(f"Current movie count: {existing_movies}")
        
        # Comprehensive movie dataset
        comprehensive_movies = [
            # Action Movies
            {
                "title": "The Dark Knight Rises",
                "original_title": "The Dark Knight Rises",
                "overview": "Eight years after the Joker's reign of anarchy, Batman, with the help of the enigmatic Catwoman, is forced from his exile to save Gotham City from the brutal guerrilla terrorist Bane.",
                "poster_url": "https://image.tmdb.org/t/p/w500/hPhfAi8I7cVnQf2qy8A5nJ6JjE9.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/fiU72sd6R7iH6jULbSyEhDaOcSa.jpg",
                "primary_genre": "Action",
                "language": "English",
                "year": 2012,
                "rating": 8.4,
                "runtime": 164
            },
            {
                "title": "Avengers: Endgame",
                "original_title": "Avengers: Endgame",
                "overview": "After the devastating events of Infinity War, the Avengers assemble once more to reverse Thanos' actions and restore balance to the universe.",
                "poster_url": "https://image.tmdb.org/t/p/w500/or06FN3Dka5tukNS1u1wHHXS878.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/7RyHsO4yDX4Bv02z9SJKkX3aQVA.jpg",
                "primary_genre": "Action",
                "language": "English",
                "year": 2019,
                "rating": 8.4,
                "runtime": 181
            },
            {
                "title": "Mission: Impossible - Fallout",
                "original_title": "Mission: Impossible - Fallout",
                "overview": "When a mission goes wrong, Ethan Hunt and his IMF team must race against time to track down a missing nuclear weapon.",
                "poster_url": "https://image.tmdb.org/t/p/w500/BbkgG5zq1v9L6U8K8t1v9L6U8K8.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5TkU5Xli9L6U8K8t1v9L6U8K8K8.jpg",
                "primary_genre": "Action",
                "language": "English",
                "year": 2018,
                "rating": 7.7,
                "runtime": 147
            },
            {
                "title": "Die Hard",
                "original_title": "Die Hard",
                "overview": "NYPD officer John McClane tries to save his wife Holly Gennaro and several others who have been taken hostage by German terrorist Hans Gruber during a Christmas party at the Nakatomi Plaza in Los Angeles.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J3.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Action",
                "language": "English",
                "year": 1988,
                "rating": 8.2,
                "runtime": 132
            },
            {
                "title": "The Terminator",
                "original_title": "The Terminator",
                "overview": "A human soldier is sent from 2029 to 1984 to stop an almost indestructible cyborg killing machine, sent from the same year, which has been programmed to execute a young woman.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Action",
                "language": "English",
                "year": 1984,
                "rating": 8.0,
                "runtime": 107
            },
            
            # Science Fiction
            {
                "title": "Blade Runner",
                "original_title": "Blade Runner",
                "overview": "A blade runner must pursue and terminate four replicants who stole a ship in space and have returned to Earth to find their creator.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Science Fiction",
                "language": "English",
                "year": 1982,
                "rating": 8.1,
                "runtime": 117
            },
            {
                "title": "Alien",
                "original_title": "Alien",
                "overview": "The commercial vessel Nostromo receives a distress call from an unexplored planet. After searching for survivors, the crew heads home only to realize that a deadly bioform has joined them.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Science Fiction",
                "language": "English",
                "year": 1979,
                "rating": 8.4,
                "runtime": 117
            },
            {
                "title": "2001: A Space Odyssey",
                "original_title": "2001: A Space Odyssey",
                "overview": "A mysterious black monolith appears on Earth in prehistoric times, and humanity's evolution is forever altered.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Science Fiction",
                "language": "English",
                "year": 1968,
                "rating": 8.3,
                "runtime": 149
            },
            {
                "title": "Star Wars: A New Hope",
                "original_title": "Star Wars: A New Hope",
                "overview": "Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, a Wookiee and two droids to save the galaxy from the Empire's world-destroying battle station.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Science Fiction",
                "language": "English",
                "year": 1977,
                "rating": 8.6,
                "runtime": 121
            },
            {
                "title": "The Empire Strikes Back",
                "original_title": "The Empire Strikes Back",
                "overview": "After the destruction of the Death Star, the Empire strikes back against the Rebel Alliance.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Science Fiction",
                "language": "English",
                "year": 1980,
                "rating": 8.7,
                "runtime": 124
            },
            
            # Drama
            {
                "title": "The Godfather: Part II",
                "original_title": "The Godfather: Part II",
                "overview": "The early life and career of Vito Corleone in 1920s New York is portrayed while his son, Michael, expands and tightens his grip on the family crime syndicate.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Drama",
                "language": "English",
                "year": 1974,
                "rating": 9.0,
                "runtime": 202
            },
            {
                "title": "Schindler's List",
                "original_title": "Schindler's List",
                "overview": "In German-occupied Poland during World War II, industrialist Oskar Schindler gradually becomes concerned for his Jewish workforce after witnessing their persecution by the Nazis.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Drama",
                "language": "English",
                "year": 1993,
                "rating": 9.0,
                "runtime": 195
            },
            {
                "title": "12 Angry Men",
                "original_title": "12 Angry Men",
                "overview": "A jury holdout attempts to prevent a miscarriage of justice by forcing his colleagues to reconsider the evidence.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Drama",
                "language": "English",
                "year": 1957,
                "rating": 9.0,
                "runtime": 96
            },
            {
                "title": "The Green Mile",
                "original_title": "The Green Mile",
                "overview": "The lives of guards on Death Row are affected by one of their charges: a black man accused of child murder and rape, yet who has a strange gift.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Drama",
                "language": "English",
                "year": 1999,
                "rating": 8.6,
                "runtime": 189
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
            
            # Thriller
            {
                "title": "The Silence of the Lambs",
                "original_title": "The Silence of the Lambs",
                "overview": "A young FBI cadet must receive the help of an incarcerated and manipulative cannibal killer to help catch another serial killer.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Thriller",
                "language": "English",
                "year": 1991,
                "rating": 8.6,
                "runtime": 118
            },
            {
                "title": "Se7en",
                "original_title": "Se7en",
                "overview": "Two detectives hunt a serial killer who uses the seven deadly sins as his motives.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Thriller",
                "language": "English",
                "year": 1995,
                "rating": 8.6,
                "runtime": 127
            },
            {
                "title": "The Usual Suspects",
                "original_title": "The Usual Suspects",
                "overview": "A sole survivor tells of the twisty events leading up to a horrific gun battle on a boat, which began when five criminals met at a seemingly random police lineup.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Thriller",
                "language": "English",
                "year": 1995,
                "rating": 8.5,
                "runtime": 106
            },
            {
                "title": "Memento",
                "original_title": "Memento",
                "overview": "A man with short-term memory loss attempts to track down his wife's murderer.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Thriller",
                "language": "English",
                "year": 2000,
                "rating": 8.4,
                "runtime": 113
            },
            {
                "title": "North by Northwest",
                "original_title": "North by Northwest",
                "overview": "A New York City advertising executive goes on the run after being mistaken for a government agent by a group of foreign spies.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Thriller",
                "language": "English",
                "year": 1959,
                "rating": 8.3,
                "runtime": 136
            },
            
            # Comedy
            {
                "title": "The Grand Budapest Hotel",
                "original_title": "The Grand Budapest Hotel",
                "overview": "A writer encounters the owner of an aging high-class hotel, who tells him of his early years serving as a lobby boy in the hotel's glorious years.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Comedy",
                "language": "English",
                "year": 2014,
                "rating": 8.1,
                "runtime": 99
            },
            {
                "title": "Dr. Strangelove",
                "original_title": "Dr. Strangelove",
                "overview": "An insane general triggers a path to nuclear holocaust that a war room full of politicians and generals frantically try to stop.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Comedy",
                "language": "English",
                "year": 1964,
                "rating": 8.4,
                "runtime": 95
            },
            {
                "title": "Monty Python and the Holy Grail",
                "original_title": "Monty Python and the Holy Grail",
                "overview": "King Arthur and his knights embark on a low-budget search for the Holy Grail, encountering many obstacles.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Comedy",
                "language": "English",
                "year": 1975,
                "rating": 8.2,
                "runtime": 91
            },
            {
                "title": "Airplane!",
                "original_title": "Airplane!",
                "overview": "A man afraid to fly must ensure that a plane lands safely after the pilots become sick.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Comedy",
                "language": "English",
                "year": 1980,
                "rating": 7.8,
                "runtime": 88
            },
            {
                "title": "The Big Lebowski",
                "original_title": "The Big Lebowski",
                "overview": "Jeff 'The Dude' Lebowski, mistaken for a millionaire of the same name, seeks restitution for his ruined rug and enlists his bowling buddies to help get it.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Comedy",
                "language": "English",
                "year": 1998,
                "rating": 8.1,
                "runtime": 117
            },
            
            # Horror
            {
                "title": "The Shining",
                "original_title": "The Shining",
                "overview": "A family heads to an isolated hotel for the winter where an evil spiritual presence influences the father into violence, while his psychic son sees horrific forebodings from both past and future.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Horror",
                "language": "English",
                "year": 1980,
                "rating": 8.4,
                "runtime": 146
            },
            {
                "title": "Psycho",
                "original_title": "Psycho",
                "overview": "A Phoenix secretary steals $40,000 from her employer's client, goes on the run and checks into a remote motel run by a young man under the domination of his mother.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Horror",
                "language": "English",
                "year": 1960,
                "rating": 8.5,
                "runtime": 109
            },
            {
                "title": "The Exorcist",
                "original_title": "The Exorcist",
                "overview": "When a teenage girl is possessed by a mysterious entity, her mother seeks the help of two priests to save her daughter.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Horror",
                "language": "English",
                "year": 1973,
                "rating": 8.1,
                "runtime": 122
            },
            {
                "title": "Aliens",
                "original_title": "Aliens",
                "overview": "When Ellen Ripley is rescued from a disaster in deep space, she discovers that the creature that attacked her crew has followed her back to Earth.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Horror",
                "language": "English",
                "year": 1986,
                "rating": 8.4,
                "runtime": 137
            },
            {
                "title": "Get Out",
                "original_title": "Get Out",
                "overview": "A young African-American visits his white girlfriend's parents for the weekend, where his simmering uneasiness about their reception eventually reaches a boiling point.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Horror",
                "language": "English",
                "year": 2017,
                "rating": 7.7,
                "runtime": 104
            },
            
            # Romance
            {
                "title": "Casablanca",
                "original_title": "Casablanca",
                "overview": "A cynical nightclub owner protects an old flame and her husband from Nazis in Morocco.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Romance",
                "language": "English",
                "year": 1942,
                "rating": 8.5,
                "runtime": 102
            },
            {
                "title": "Titanic",
                "original_title": "Titanic",
                "overview": "A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Romance",
                "language": "English",
                "year": 1997,
                "rating": 7.9,
                "runtime": 194
            },
            {
                "title": "The Notebook",
                "original_title": "The Notebook",
                "overview": "A poor yet passionate young man falls in love with a rich young woman, giving her a sense of freedom, but they are soon separated because of their social differences.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Romance",
                "language": "English",
                "year": 2004,
                "rating": 7.8,
                "runtime": 123
            },
            {
                "title": "La La Land",
                "original_title": "La La Land",
                "overview": "While navigating their careers in Los Angeles, a pianist and an actress fall in love while attempting to reconcile their aspirations for the future.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Romance",
                "language": "English",
                "year": 2016,
                "rating": 8.0,
                "runtime": 128
            },
            {
                "title": "Eternal Sunshine of the Spotless Mind",
                "original_title": "Eternal Sunshine of the Spotless Mind",
                "overview": "When their relationship turns sour, a couple undergoes a medical procedure to have each other erased from their memories.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Romance",
                "language": "English",
                "year": 2004,
                "rating": 8.3,
                "runtime": 108
            },
            
            # Adventure
            {
                "title": "Indiana Jones: Raiders of the Lost Ark",
                "original_title": "Indiana Jones: Raiders of the Lost Ark",
                "overview": "Archaeologist and adventurer Indiana Jones is hired by the U.S. government to find the Ark of the Covenant before the Nazis.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Adventure",
                "language": "English",
                "year": 1981,
                "rating": 8.4,
                "runtime": 115
            },
            {
                "title": "Jurassic Park",
                "original_title": "Jurassic Park",
                "overview": "During a preview tour, a theme park suffers a major power breakdown that allows its cloned dinosaur exhibits to run loose.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Adventure",
                "language": "English",
                "year": 1993,
                "rating": 8.1,
                "runtime": 127
            },
            {
                "title": "The Lord of the Rings: The Fellowship of the Ring",
                "original_title": "The Lord of the Rings: The Fellowship of the Ring",
                "overview": "A meek Hobbit from the Shire and eight companions set out on a journey to destroy the powerful One Ring and save Middle-earth.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Adventure",
                "language": "English",
                "year": 2001,
                "rating": 8.8,
                "runtime": 178
            },
            {
                "title": "The Lord of the Rings: The Two Towers",
                "original_title": "The Lord of the Rings: The Two Towers",
                "overview": "While Frodo and Sam continue their journey to destroy the One Ring, members of the Fellowship are separated and must prepare for the coming war.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Adventure",
                "language": "English",
                "year": 2002,
                "rating": 8.7,
                "runtime": 179
            },
            {
                "title": "Pirates of the Caribbean: The Curse of the Black Pearl",
                "original_title": "Pirates of the Caribbean: The Curse of the Black Pearl",
                "overview": "Blacksmith Will Turner teams up with eccentric pirate 'Captain' Jack Sparrow to save his love, the governor's daughter, from Jack's former pirate allies.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Adventure",
                "language": "English",
                "year": 2003,
                "rating": 8.1,
                "runtime": 143
            },
            
            # Mystery
            {
                "title": "Chinatown",
                "original_title": "Chinatown",
                "overview": "A private detective hired to expose an adulterer finds himself caught up in a web of deceit, corruption, and murder.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Mystery",
                "language": "English",
                "year": 1974,
                "rating": 8.1,
                "runtime": 130
            },
            {
                "title": "Rear Window",
                "original_title": "Rear Window",
                "overview": "A wheelchair-bound photographer spies on his neighbors from his apartment window and becomes convinced one of them has committed murder.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Mystery",
                "language": "English",
                "year": 1954,
                "rating": 8.5,
                "runtime": 112
            },
            {
                "title": "Vertigo",
                "original_title": "Vertigo",
                "overview": "A former police detective juggles his crippling fear of heights and an obsession with a beautiful woman.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Mystery",
                "language": "English",
                "year": 1958,
                "rating": 8.3,
                "runtime": 128
            },
            {
                "title": "Zodiac",
                "original_title": "Zodiac",
                "overview": "Based on the true story of the hunt for a serial killer who terrorized the San Francisco Bay Area during the late 1960s and early 1970s.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Mystery",
                "language": "English",
                "year": 2007,
                "rating": 7.7,
                "runtime": 157
            },
            {
                "title": "Gone Girl",
                "original_title": "Gone Girl",
                "overview": "With his wife's disappearance having become the focus of an intense media circus, a man sees the spotlight turned on him when it's suspected that he may not be innocent.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Mystery",
                "language": "English",
                "year": 2014,
                "rating": 8.1,
                "runtime": 149
            },
            
            # Crime
            {
                "title": "The Departed",
                "original_title": "The Departed",
                "overview": "An undercover cop and a mole in the police attempt to identify each other while infiltrating an Irish gang in South Boston.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Crime",
                "language": "English",
                "year": 2006,
                "rating": 8.5,
                "runtime": 151
            },
            {
                "title": "Scarface",
                "original_title": "Scarface",
                "overview": "A determined Cuban immigrant takes over a drug empire while succumbing to greed.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Crime",
                "language": "English",
                "year": 1983,
                "rating": 8.3,
                "runtime": 170
            },
            {
                "title": "Casino",
                "original_title": "Casino",
                "overview": "An expert gambler is hired by a crime syndicate to run a casino in Las Vegas, but his relationship with his wife becomes complicated.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Crime",
                "language": "English",
                "year": 1995,
                "rating": 8.2,
                "runtime": 178
            },
            {
                "title": "Reservoir Dogs",
                "original_title": "Reservoir Dogs",
                "overview": "After a simple jewelry heist goes terribly wrong, the surviving criminals begin to suspect that one of them is a police informant.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Crime",
                "language": "English",
                "year": 1992,
                "rating": 8.3,
                "runtime": 99
            },
            {
                "title": "Heat",
                "original_title": "Heat",
                "overview": "A group of professional bank robbers start to feel the heat from police when they unknowingly leave a clue at their latest heist.",
                "poster_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "backdrop_url": "https://image.tmdb.org/t/p/w500/5yK4Y3Q3J3J3J3J3J3J3J3J3J.jpg",
                "primary_genre": "Crime",
                "language": "English",
                "year": 1995,
                "rating": 8.3,
                "runtime": 170
            }
        ];
        
        # Add movies to database
        added_count = 0
        for movie_data in comprehensive_movies:
            # Check if movie already exists
            existing = db.query(Movie).filter(Movie.title == movie_data["title"]).first()
            if not existing:
                movie = Movie(**movie_data)
                db.add(movie)
                added_count += 1
        
        db.commit()
        print(f"Added {added_count} new movies to database")
        print(f"Total movies in database: {db.query(Movie).count()}")
        
    except Exception as e:
        print(f"Error adding comprehensive movies: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_comprehensive_movies()
