from show import Show


class Screen:

    def __init__(self, id,  screen_number, total_seat: int):
        self.id = id
        self.screen = {}
        self.seat = {}
        self.screen_number = screen_number
        self.shows = []

    def __str__(self) -> str:
        return self.id
    
    def add_movie(self, movie: object,  start_datetime, end_datetime):
        Show().check_overlap(self.shows, start_datetime, end_datetime)
        show = Show(movie_obj=movie, start_time=start_datetime, end_time=end_datetime)
        self.shows.append(show)
    
    def add_seat(self, seat_obj: object, seat_type: str):
        
        if self.seat.get(seat_type):
            seat_data = self.seat[seat_type]
            seat_data.append(seat_obj)
        else:   
            self.seat[seat_type] = [seat_obj]
        

    def display_seat(self):
        for key, seat_array in self.seat.items():
            print(f"Seat Type: {key}")
            for seat in seat_array:
                print(f"Number {seat.seat_number}")