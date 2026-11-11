from uuid import uuid4
from datetime import datetime, timedelta
from MovieGenere import MovieGenere, Movie
from Theater import Theater
from Screen import Screen
from Seat import SeatFactory, SeatType
from show import Show
from User import User
theater = Theater(uuid4(), "dlf mall", "gurgaon")

screen_1 = Screen(uuid4(), "screen 1", "100")
screen_2 = Screen(uuid4(), "screen 2", "200")
screen_3 = Screen(uuid4(), "screen 3", "300")

theater.add_screen(screen_key = "screen 1", screen_obj = screen_1)
theater.add_screen(screen_key = "screen 2", screen_obj = screen_2)
theater.add_screen(screen_key = "screen 3", screen_obj = screen_3)

movie_obj_1 = Movie(id = uuid4(), movie_name = "Ramayana", movie_language = "Hindi", movie_genere = [MovieGenere.Spirtual.value], movie_duration = "2 hours 45 minutes", imdb_rating = 10, relese_date = "16-oct-2026")
movie_obj_2 = Movie(id = uuid4(), movie_name = "Mahabharat", movie_language = "Hindi", movie_genere = [MovieGenere.Spirtual.value], movie_duration = "2 hours 45 minutes", imdb_rating = 10, relese_date = "16-oct-2026")
movie_obj_3 = Movie(id = uuid4(), movie_name = "Odyssey", movie_language = "Hindi", movie_genere = [MovieGenere.Spirtual.value], movie_duration = "2 hours 45 minutes", imdb_rating = 10, relese_date = "16-oct-2026")
movie_obj_4 = Movie(id = uuid4(), movie_name = "Golmal", movie_language = "Hindi", movie_genere = [MovieGenere.Comedy.value], movie_duration = "2 hours 45 minutes", imdb_rating = 10, relese_date = "16-oct-2026")





theater.add_movie(movie_obj=movie_obj_1)
theater.add_movie(movie_obj=movie_obj_2)
theater.add_movie(movie_obj=movie_obj_3)
theater.add_movie(movie_obj=movie_obj_4)

screen_1_show1_starttime = datetime.strptime("16-oct-2026 9:00", "%d-%b-%Y %H:%M")
screen_1_show1_endtime = datetime.strptime("16-oct-2026 12:00", "%d-%b-%Y %H:%M")

screen_1_show2_starttime = datetime.strptime("16-oct-2026 13:00", "%d-%b-%Y %H:%M")
screen_1_show2_endtime = datetime.strptime("16-oct-2026 16:00", "%d-%b-%Y %H:%M")

screen_1_show3_starttime = datetime.strptime("16-oct-2026 17:00", "%d-%b-%Y %H:%M")
screen_1_show3_endtime = datetime.strptime("16-oct-2026 20:00", "%d-%b-%Y %H:%M")


screen_1.add_movie(movie_obj_1, screen_1_show1_starttime, screen_1_show1_endtime)
screen_1.add_movie(movie_obj_1, screen_1_show2_starttime, screen_1_show2_endtime)
screen_1.add_movie(movie_obj_1, screen_1_show3_starttime, screen_1_show3_endtime)

user = User("9525700120").create_user("mk2747@gmail.com", "kashif decosta")



reclinear = SeatFactory().initilize("reclinear", "1200", "1")
middle = SeatFactory().initilize("middle", "600", "2")
front = SeatFactory().initilize("front", "300", "3")


screen_1.add_seat(reclinear, "reclinear")
screen_1.add_seat(middle, "middle")
screen_1.add_seat(front, "front")


# screen_1_start_datetime_morning = datetime.strptime("16-oct-2026 9:00", "%d-%b-%Y %H:%M")
# screen_1_end_datetime_morning = screen_1_start_datetime_morning + timedelta(minutes=400)

# screen_2_start_datetime_afternoon = datetime.strptime("16-oct-2026 12:00", "%d-%b-%Y %H:%M")
# screen_2_end_datetime_afternoon = screen_2_start_datetime_afternoon + timedelta(minutes=400)

# screen_3_start_datetime_evening = datetime.strptime("16-oct-2026 14:00", "%d-%b-%Y %H:%M")
# screen_3_end_datetime_evening = screen_3_start_datetime_evening + timedelta(minutes=400)

# screen_4_start_datetime_night = datetime.strptime("16-oct-2026 18:00", "%d-%b-%Y %H:%M")
# screen_4_end_datetime_night = screen_4_start_datetime_night + timedelta(minutes=400)



# screen_1.add_movie(movie_obj_1, screen_1_start_datetime_morning, screen_1_end_datetime_morning, movie_mode = "morning")
# screen_1.add_movie(movie_obj_2, screen_2_start_datetime_afternoon, screen_2_end_datetime_afternoon, movie_mode = "afternoon")
# screen_1.add_movie(movie_obj_3, screen_3_start_datetime_evening, screen_3_end_datetime_evening, movie_mode = "evening")
# screen_1.add_movie(movie_obj_4, screen_4_start_datetime_night, screen_4_end_datetime_night, movie_mode = "night")



# screen_2_start_datetime_morning = datetime.strptime("16-oct-2026 9:00", "%d-%b-%Y %H:%M")
# screen_2_end_datetime_morning = screen_2_start_datetime_morning + timedelta(minutes=400)

# screen_2_start_datetime_afternoon = datetime.strptime("16-oct-2026 12:00", "%d-%b-%Y %H:%M")
# screen_2_end_datetime_afternoon = screen_2_start_datetime_afternoon + timedelta(minutes=400)

# screen_2_start_datetime_evening = datetime.strptime("16-oct-2026 14:00", "%d-%b-%Y %H:%M")
# screen_2_end_datetime_evening = screen_2_start_datetime_evening + timedelta(minutes=400)

# screen_2_start_datetime_night = datetime.strptime("16-oct-2026 18:00", "%d-%b-%Y %H:%M")
# screen_2_end_datetime_night = screen_2_start_datetime_night + timedelta(minutes=400)

# screen_2.add_movie(movie_obj_1, screen_2_start_datetime_morning, screen_2_end_datetime_morning, movie_mode = "morning")
# screen_2.add_movie(movie_obj_2, screen_2_start_datetime_afternoon, screen_2_end_datetime_afternoon, movie_mode = "afternoon")
# screen_2.add_movie(movie_obj_3, screen_2_start_datetime_evening, screen_2_end_datetime_evening, movie_mode = "evening")
# screen_2.add_movie(movie_obj_4, screen_2_start_datetime_night, screen_2_end_datetime_night, movie_mode = "night")


# screen_3_start_datetime_morning = datetime.strptime("16-oct-2026 9:00", "%d-%b-%Y %H:%M")
# screen_3_end_datetime_morning = screen_3_start_datetime_morning + timedelta(minutes=400)

# screen_3_start_datetime_afternoon = datetime.strptime("16-oct-2026 12:00", "%d-%b-%Y %H:%M")
# screen_3_end_datetime_afternoon = screen_3_start_datetime_afternoon + timedelta(minutes=400)

# screen_3_start_datetime_evening = datetime.strptime("16-oct-2026 14:00", "%d-%b-%Y %H:%M")
# screen_3_end_datetime_evening = screen_3_start_datetime_evening + timedelta(minutes=400)

# screen_3_start_datetime_night = datetime.strptime("16-oct-2026 18:00", "%d-%b-%Y %H:%M")
# screen_3_end_datetime_night = screen_3_start_datetime_night + timedelta(minutes=400)

# screen_3.add_movie(movie_obj_1, screen_3_start_datetime_morning, screen_3_end_datetime_morning, movie_mode = "morning")
# screen_3.add_movie(movie_obj_2, screen_3_start_datetime_afternoon, screen_3_end_datetime_afternoon, movie_mode = "afternoon")
# screen_3.add_movie(movie_obj_3, screen_3_start_datetime_evening, screen_3_end_datetime_evening, movie_mode = "evening")
# screen_3.add_movie(movie_obj_4, screen_3_start_datetime_night, screen_3_end_datetime_night, movie_mode = "night")





#show_obj = Show(movie_obj, start_datetime, end_datetime)







