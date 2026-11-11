Functional Requirement
1.	We can have movie
2.	Theatre has a screen (Map)   Location, movie 
3.	Screen (have a seat, movie)
4.	Seat can be of different type -> Recliner, simple
5.	Seat can be Vacant, booked, Selected TTL
6.	Seat with Selected State will be locked for a particular TTL  (5min) 
7.	Payment (We have to manange multiple payment aggregator)
8.	Implement a functionality of seat locked 
9.	We maintain ticket reposotiory (it is to maintain which ticket is locked and what is ttl how much is left)
10.	Before payment we should check if seat is still available or not 
11.	 Released lock in payment fail etc

user : A

seat: select kari oooo 4, 5, 6


user : b

seat: 6, 7, 8



shows1: start_time: 9'o clock end_time: 10:55'o clock


shows2: start_time: 11'o clock , end_time: 2'o clock




shows3: start_tome: 10:59'o clock, end_time: 12'o clock



