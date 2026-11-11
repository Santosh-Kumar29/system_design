from enum import Enum


class MovieGenere(Enum):
    Erotic = "Erotic"
    Comedy = "Comedy"
    Romance = "Romance"
    Thrilller = "Thriller"
    Spirtual = "Spirtual"
    History = "History"


class Movie:

    def __init__(self, id,  movie_name, movie_language, movie_genere: [], movie_duration, imdb_rating, relese_date):
        self.id = id
        self.movie_name = movie_name
        self.movie_language = movie_language
        self.movie_genere = movie_genere
        self.movie_duration = movie_duration
        self.imdb_rating = imdb_rating
        
        
        


