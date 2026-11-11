

from abc import abstractmethod, ABC
from uuid import uuid4



## vehicle
class VehcileType:
    SMALL = "SMALL"
    MEDIUM = "MEDIUM"
    LARGE = "LARGE"


## find spot


class SpotStatePattern(ABC):
    @abstractmethod
    def occupy(self, spot):
        pass
    @abstractmethod
    def free(self, spot):
        pass
    

class FreeState(SpotStatePattern):
    def occupy(self, spot):
        spot.state = OccupiedState()
        
    def free(self, spot):
        raise Exception("Spot is already free")
    
    
class OccupiedState(SpotStatePattern):
    def occupy(self, spot):
        raise Exception("spot is already occupied")
    
    def free(self, spot):
        spot.state = FreeState()
    
# class Spot:
#     def __init__(self, spot_type) -> None:
#         self.spot_type = spot_type
#         self.is_occupy = False
#         self.is_free  =True
        
#     def occupy(self):
#         pass
    
#     def free(self):
#         pass
    


## handle floor 
class Floor:
    
    def __init__(self, floor_number) -> None:
        self.floor_number = floor_number
        self.spot = []
        
    
    def add_spot(self, spot):
        self.spot.append(spot)
        
    def availeb_spot(self):
       return [spot for spot in self.spot.is_free()] 



## handle find parking spot
class ParkingLot(ABC):
    @abstractmethod
    def find_spot(self):
        pass
    
    
class ProrityParkingSpot(ParkingLot):
    def find_spot(self):
        pass

class NearestParkingSpot(ParkingLot):
    def find_spot(self):
        pass
    
class ParkingSpot:
    
    def __init__(self, floor: Floor, parking_lot: ParkingLot) -> None:
        self.floor = floor
        self.parking_lot  = parking_lot
        self.vehicle = None
        self.state = FreeState()
        
    
    def set_parking_lot(self, parking_lot):
        self.parking_lot = parking_lot
        
    
    def occupy(self, vehicle):
        pass
    
    def free(self, vehicle):
        pass
    
    def is_free(self):
        if FreeState(self.state):
            return True
        else:
            False


## vehicle categories

class Vehicle:
    def __init__(self, vehicle_number,  vehicle_type: VehcileType) -> None:
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type

class Tickets:
    pass




## entry the vehcile

class EntryGate:
    def __init__(self, ticket: Tickets, vehicle: Vehicle, ParkingLpot: ParkingSpot, entry_time) -> None:
        self.ticket = ticket
        self.vehicle = vehicle
        self.parking_spot = ParkingLpot
        self.entry_time = entry_time
        
    def park_vehcicle(self):
        pass


# handle the payemtnt
class PaymentScenario(ABC):
    @abstractmethod
    def calcualte_price(self):
        pass
    
    
class PeakHours(PaymentScenario):
    def __init__(self, total_time, vehicle: Vehicle):
        self.total_time = total_time
        self.vehicle  = vehicle
        
    def calcualte_price(self):
        pass
 
     
class Weekend(PaymentScenario):
    def __init__(self, total_time, vehicle: Vehicle):
        self.total_time = total_time
        self.vehicle  = vehicle
        
    def calcualte_price(self):
        pass   
    
class PaymentHandler:
    def __init__(self, payment:PaymentScenario ) -> None:
        
        self.payment_scenario = payment
        
        
    def set_payemnt_handle(self, payment_scenario):
        self.payment_scenario  = payment_scenario
        


## exit the gate
class ExitGate:
    def __init__(self, ticket: Tickets, vehicle: Vehicle, ParkingLpot: ParkingSpot, entry_time) -> None:
        self.ticket = ticket
        self.vehicle = vehicle
        self.parking_spot = ParkingLpot
        self.entry_time = entry_time
        
    def unpark_vehicle(self):
        pass

    