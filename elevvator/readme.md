Elevator System Design

Functional requirement 
Elevator Controller 
Elevator 
Request
	-> Hall Request  (Floor request (Up, Down))
	-> inside request (Floor Number)


class EleveatorState:
    UP
    DOWN
    IDLE


ElevatorController

    elevator []

    0 - 9 floor 

    request - func - accept karega request arg 
    

Elevator System Design

Functional requirement 
Elevator Controller
Elevator 
Request
	-> Hall Request  (Floor request (Up, Down))
	-> inside request (Floor Number)






Request
	type  -> Inside/ hall
	direction -> Up/down/None
	floor -> number


santosh Sir-> 4th floor Up (hall)



Elevator Controller
	constructor (dispatchRequerstStrtegy)
	Elevator[3]
	floor [] 0-9
	dispatch_request(R1 Request):
		dispatchRequerstStrtegy.dispatchRequest(request, Elevator)


Elevator
	requet[]
	floor
	direction
	add_request(request)
	
	
		

E1, E2, E3


2 
shortest distance

floor request  - 5 

E1  -> 8
E2 -> 3
E3 -> 6


Shortest Distance with direction
floor request  - 5

E1  -> 8 -> Down  (preferenc   distance -> 3)
E2 -> 3 -> Up    (distance 2 preferece
E3 -> 6 -> Up   (distance 1)X

