class Theater:
    def __init__(self, id,  theater_name, theater_location):
        self.id = id
        self.theater_name = theater_name
        self.theater_location = theater_location
        self.screen = {}
        self.movies = []
        
    def __str__(self) -> str:
        return self.id
    def add_screen(self, screen_obj, screen_key):
        self.screen[screen_key] = screen_obj
    
    def add_movie(self, movie_obj):
        self.movies.append(movie_obj)
        
    
    def get_screen(self, screen_key):
        return self.screen.get(screen_key, None)
    
    def list_all_movie(self, screen_key):
        return self.movies
            
    