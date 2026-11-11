from abc import ABC, abstractmethod
from enum import Enum
from re import L
from uuid import uuid4


class SeatType(Enum):
    RECLINEAR = "RECLINEAR"
    MIDDLE = "MIDDLE"
    FRONT = "FRONT"


class Seat(ABC):

    def __init__(self, seat_number):
        self.id = uuid4()
        self.seat_number = seat_number

    @abstractmethod
    def seat_type(self):
        pass

    @abstractmethod
    def amount(self):
        pass
    

class Recliner(Seat):
    
    def __init__(self, seat_type, amount, seat_number):
        self.seat_type = seat_type
        self.amount = amount
        super().__init__(seat_number=seat_number)

    def seat_type(self, seat_type):
        self.seat_type = seat_type


    def amount(self, amount):
        self.amount = amount

class Middle(Seat):
    
    def __init__(self, seat_type, amount, seat_number):
        self.seat_type = seat_type
        self.amount = amount
        super().__init__(seat_number=seat_number)

    def seat_type(self, seat_type):
        self.seat_type = seat_type


    def amount(self, amount):
        self.amount = amount
        
class Front(Seat):

    def __init__(self, seat_type, amount, seat_number):
        self.seat_type = seat_type
        self.amount = amount
        super().__init__(seat_number=seat_number)
        
    def seat_type(self, seat_type):
        self.seat_type = seat_type


    def amount(self, amount):
        self.amount = amount
        

class SeatFactory:
    
    def __init__(self):
        self.cls = {"reclinear": Recliner, "middle": Middle, "front": Front }
         
        

    def initilize(self, seat_type, amount, seat_number):
        
        if self.cls.get(seat_type, None):
            seat_cls =  self.cls.get(seat_type)
            return seat_cls(seat_type, amount, seat_number)
            
            