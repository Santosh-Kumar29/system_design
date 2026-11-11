# ## fcfs - first come first serve

# from collections import deque


# class Choice(Enum):
#     MOVING = "MOVING"
#     IDLE = "IDLE"

# class Direction(Enum):
#     UP = "UP"
#     DOWN = "DOWN"
  
# ## elevator dipatcher
# class Elevator:
#     def __init__(self):
#         self.request = deque()
#         self.current_floor = 0
#         self.pos = Choice.IDLE.value()
#         self.direction = Direction.UP.value()
    
#     ## this floor number represet wherveer the evevator will go
#     def add_request(self, floor_number):

#         self.request.append(floor_number)

#     def get_next_floor(self):
#         return self.request.popleft()

#     def move_floor(self):

#         while len(self.request) != 0:
#           next_floor = self.get_next_floor(). ## floor request
#           if next_flor < self.current_floor:
#               self.direction = Direction.DOWN.value()
#           else:
#               self.direction - Direction.UP.value()
#           self.pos = Choice.MOVING.value()

#           number_of_steps = abs(self.current_floor - next_floor)

#           for i in range(number_of_steps):
#             if self.direction == Direction.UP.Value:
#               self.current_floor ++
#             else:
#               self.current_floor --

#           print("floor reached", self.current_floor)

          
      

          

# ## stsf - shortest seek time first


# ##stsf
# from collections import deque


# class Choice(Enum):
#     MOVING = "MOVING"
#     IDLE = "IDLE"

# class Direction(Enum):
#     UP = "UP"
#     DOWN = "DOWN"
  
# ## elevator dipatcher
# class Elevator:
#     def __init__(self):
#         self.request = []
#         self.current_floor = 0
#         self.pos = Choice.IDLE.value()
#         self.direction = Direction.UP.value()
    
#     ## this floor number represet wherveer the evevator will go
#     def add_request(self, floor_number):

#         self.request.append(floor_number)

#     def get_next_floor(self):
#       min_floor = float('inf')
#       next_floor = None
#       for floor in self.request:
#         distance = abs(self.currrent_floor - floor)
      
#         if min_floor > distance:
#           min_floor = distance 
#           next_floor = floor

#       return next_floor
             
          
#         #return self.request.popleft()

#     def move_floor(self):

#         while len(self.request) != 0:
#           next_floor = self.get_next_floor(). ## floor request
#           if next_flor < self.current_floor:
#               self.direction = Direction.DOWN.value()
#           else:
#               self.direction - Direction.UP.value()
#           self.pos = Choice.MOVING.value()

#           number_of_steps = abs(self.current_floor - next_floor)

#           for i in range(number_of_steps):
#             if self.direction == Direction.UP.Value:
#               self.current_floor ++
#             else:
#               self.current_floor --

#           print("floor reached", self.current_floor)
#           self.request.remove(next_floor)

          
      

          

  