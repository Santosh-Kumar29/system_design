from uuid import uuid4


class Show:
    
    def __init__(self, movie_obj, start_time, end_time):
        self.id = uuid4()
        self.movie_obj = movie_obj
        self.start_time = start_time
        self.end_time = end_time
        
    
    def check_overlap(self, shows, start_time, end_time):
        for show in shows:
            ## [10-2, 3- 7]
            # 9 pm, 6pm
            if start_time < show.start_time and end_time > show.start_time:
                raise Exception("this time slot is already reserved")
                
        
    