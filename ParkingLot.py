from abc import abstractmethod, abc
from enum import Enum

# class VehicleType(Enum):
#     SMALL = "SMALL"
#     MEDIUM = "MEDIUM"
#     LARGE = "LARGE"

        
# class VehicleType(abc):
        
#     @abstractmethod
#     def getVehicle(self):
#         pass

# class SmallVehicle(VehicleType):
    
#     def __init__(self, vehicle_number):
#         self.vehicle = VehicleType.SMALL.value
#         self.vehicle_number = vehicle_number
    
    
#     def get_vehicle(self):
#         return self.vehicle_number, self.vehicle

# class MediumVehicle(VehicleType):
    
#     def __init__(self, vehicle_number):
#         self.vehicle = VehicleType.MEDIUM.value
#         self.vehicle_number = vehicle_number
    
    
#     def get_vehicle(self):
#         return self.vehicle_number, self.vehicle


# class LargeVehicle(VehicleType):
    
#     def __init__(self, vehicle_number):
#         self.vehicle = VehicleType.LARGE.value
#         self.vehicle_number = vehicle_number
    
#     def get_vehicle(self):
#         return self.vehicle_number, self.vehicle

## with floor and row and column
from abc import ABC, abstractmethod
import uuid
from datetime import datetime

class VehicleType(Enum):
    SMALL = "SMALL"
    MEDIUM = "MEDIUM"
    LARGE = "LARGE"


class ParkingSlotType(Enum):
    SMALL = "SMALL"
    MEDIUM = "MEDIUM"
    LARGE = "LARGE"


class Floor(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    

class Vehicle:

    def __init__(self, vehicle_number, vehicle_type):
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type

    def __str__(self):
        return f"{self.vehicle_number} ({self.vehicle_type.value})"
    
    

class ParkingSlot:

    def __init__(self, slot_id, slot_type, floor, row, column):
        self.slot_id = slot_id
        self.slot_type = slot_type
        self.floor = floor
        self.row = row
        self.column = column

        self.vehicle = None
        self.available = True

    def is_available(self):
        return self.available

    def park_vehicle(self, vehicle):

        if not self.available:
            raise Exception("Parking slot already occupied")

        self.vehicle = vehicle
        self.available = False

    def unpark_vehicle(self):

        if self.available:
            raise Exception("Parking slot is already empty")

        vehicle = self.vehicle
        self.vehicle = None
        self.available = True

        return vehicle

    def __str__(self):
        return f"Slot-{self.slot_id} [{self.slot_type.value}]"
    
    

class ParkingTicket:

    def __init__(self, vehicle, slot):

        self.ticket_id = str(uuid.uuid4())

        self.vehicle = vehicle
        self.slot = slot

        self.entry_time = datetime.now()
        self.exit_time = None

    def close_ticket(self):
        self.exit_time = datetime.now()
        
        

class ParkingStrategy(ABC):

    @abstractmethod
    def find_slot(self, vehicle, slots):
        pass



class FirstAvailableParkingStrategy(ParkingStrategy):

    def find_slot(self, vehicle, slots):

        for slot in slots:

            if (
                slot.is_available()
                and slot.slot_type.value == vehicle.vehicle_type.value
            ):
                return slot

        return None
    
class Payment:

    def __init__(self, amount):
        self.amount = amount

    def make_payment(self):
        print(f"Payment Successful : ₹{self.amount}")
        

class ParkingLot:

    def __init__(self, lot_id, name, address, strategy):

        self.lot_id = lot_id
        self.name = name
        self.address = address

        self.strategy = strategy

        self.slots = []

        self.active_tickets = {}

    def add_slot(self, slot):
        self.slots.append(slot)

    def park_vehicle(self, vehicle):

        slot = self.strategy.find_slot(vehicle, self.slots)

        if slot is None:
            raise Exception("No parking slot available")

        slot.park_vehicle(vehicle)

        ticket = ParkingTicket(vehicle, slot)

        self.active_tickets[ticket.ticket_id] = ticket

        print(f"Vehicle Parked Successfully")
        print(f"Ticket ID : {ticket.ticket_id}")
        print(f"Allocated Slot : {slot.slot_id}")

        return ticket

    def unpark_vehicle(self, ticket_id):

        if ticket_id not in self.active_tickets:
            raise Exception("Invalid Ticket")

        ticket = self.active_tickets[ticket_id]

        ticket.slot.unpark_vehicle()

        ticket.close_ticket()

        amount = self.calculate_fee(ticket)

        Payment(amount).make_payment()

        del self.active_tickets[ticket_id]

        print("Vehicle Unparked Successfully")

    def calculate_fee(self, ticket):

        duration = (ticket.exit_time - ticket.entry_time).seconds

        hours = max(1, duration // 3600)

        return hours * 100

    def get_vehicle_count(self):
        return len(self.active_tickets)

    def get_vehicle_count_by_type(self, vehicle_type):

        count = 0

        for ticket in self.active_tickets.values():

            if ticket.vehicle.vehicle_type == vehicle_type:
                count += 1

        return count
