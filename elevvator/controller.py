# Request
# 	type  -> Inside/ hall
# 	direction -> Up/down/None
# 	floor -> number


# santosh Sir-> 4th floor Up (hall)



# Elevator Controller
# 	constructor (dispatchRequerstStrtegy)
# 	Elevator[3]
# 	floor [] 0-9
# 	dispatch_request(R1 Request):
# 		dispatchRequerstStrtegy.dispatchRequest(request, Elevator)


from enum import Enum

class RequestType(Enum):
    INSIDE = "inside"
    HALL = "hall"
    
    
class RequestDirection(Enum):
    UP = "up"
    DOWN = "down"
    NONE  = "none"
  
class Elevator:

  def __init__(self, id, total_floor):
    self.id = id
    self.current_floor = 0

    self.total_floor = total_floor

    def move_down(self):
      self.current_floor -= 1

    def move_up(self):
      self.current_floor += 1
      
    def get_current_floor(self):
      return self.current_floor
  
    def get_direction(self):
      if self.current_floor > self.target_floor:
        return RequestDirection.DOWN
      elif self.current_floor < self.target_floor:
        return RequestDirection.UP
      else:
        return RequestDirection.NONE


class ElevatorController:

  def __init__(self, ):
    self.elvevator = [Elevator(1, 10) for i  in range(3)]


  def request_elevator(self, request):
    if request.type == RequestType.INSIDE:
      self.elvevator[0].request(request.floor)
    else:
      self.elvevator[0].request(request.floor)
      

from abc import ABC, abstractmethod
      
class LiftStrategy(ABC):
  
  @abstractmethod
  def get_next_floor(self, request):
    pass
  
## [1, 2, 4,5, 4, 3, 6]

class Request:
  def __init__(self, floor, type, direction):
    self.floor = floor
    self.type = type
    self.direction = direction
  
  
  


class FCFSLiftStrategy(LiftStrategy):
  
  def get_next_floor(self, request):
    return request[0]
  

class ShortestDistanceRequestAssignmener(LiftStrategy):
    
  def assign_request(self, request: Request, elevators):
    min_floor = float("inf")
    min_elv = None
    for elevator in elevators:
      current_floor = elevator.get_current_floor()
      get_floor = abs(current_floor - request.floor)
      if get_floor < min_floor:
        min_floor = get_floor
        min_elv = elevator
    min_elv.add_request(request)


## strategy pattern, sigelton pattern, state pattern, observer pattern, factory pattern, builder pattern, adapter pattern, decorator pattern
## first we check the request is  form which floor
## let say it come from 6th floor

## first we find all the lift which is top from 6th floor and its direction is down or idle 

## and also we need to find that the lift which is on top and also whats there direction means there direction should be down 

## and so on after that we find the min distane between current floor and the lift requested floor

## same for lower floor lift which have up direction

## and finally we calcuate the min ditace and attach with the lift


# class FindAllClosestLiftDistance:

#   def find_list(self, request: Request, elevators):
#     top_lift = []
#     botton_lift = []

#     for elevator in elevators:
#       current_floor = elevator.get_current_floor()
#       if current_floor > request.floor and elevator.get_direction == DOWN and elevator.get_direction == IDLE:
        
    
    

    
    
    
    

    
    
    