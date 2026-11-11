from abc import ABC, abstractmethod
import uuid
from datetime import datetime
from enum import Enum


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
    
    def get_vehicle_number(self):
        return self.vehicle_number
    
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
    def __init__(self, ticket_id, vehicle, slot, entry_time, exit_time):
        self.ticket_id = ticket_id
        self.vehicle = vehicle
        self.slot = slot
        self.entry_time = entry_time
        self.exit_time = exit_time
    
    def get_ticket_id(self):
        return self.ticket_id
    
    def get_vehicle(self):
        return self.vehicle
        
    def close_ticket(self):
        self.exit_time = datetime.now()
        return self.exit_time
    
    def get_entry_time(self):
        return self.entry_time
    
    def get_exit_time(self):
        return self.exit_time
    
    def __str__(self):
        return f"Ticket-{self.ticket_id} [{self.vehicle.get_vehicle_number()}] [{self.slot.get_slot_id()}] [{self.entry_time}] [{self.exit_time}]"
    
## missing floor and row and column
class ParkingStrategy(ABC):
    @abstractmethod
    def find_slot(self, vehicle, slots):
        pass

class FirstAvailableParkingStrategy(ParkingStrategy):
    def find_slot(self, vehicle, slots):
        for slot in slots:
            if slot.is_available() and slot.slot_type.value == vehicle.vehicle_type.value:
                return slot
        return None


    
class PaymentStrategy(ABC):
    @abstractmethod
    def calcualte_price(self):
        pass
    

class PeakHourPricing(PaymentStrategy):

    def calculate_price(self, total_hours):
        return total_hours * 150
    
class WeekendPricing(PaymentStrategy):

    def calculate_price(self, total_hours):
        return total_hours * 250
    
class WeekdayPricing(PaymentStrategy):

    def calculate_price(self, total_hours):
        return total_hours * 100
    

class Payment:
    def __init__(self, totla_hours):
        self.totla_hours = totla_hours
    
    def make_payment(self, payment_strategy):
        final_price = payment_strategy.calculate_price(self.totla_hours)
        print(f"Payment Successful : ₹{final_price}")
    
    def __str__(self):
        return f"Payment-{self.amount}"
class ParkingLot:
    def __init__(self, lot_id, name, address, strategy, payment_strategy: ParkingStrategy):
        self.lot_id = lot_id
        self.name = name
        self.address = address
        self.strategy = strategy
        self.slots = []
        self.active_tickets = {}
        self.payment_strategy = payment_strategy
    
    def add_slot(self, slot):
        self.slots.append(slot)
    
    def park_vehicle(self, vehicle):
        
        slot = self.strategy.find_slot(vehicle, self.slots)
        if slot is None:
            raise Exception("No parking slot available")
        slot.park_vehicle(vehicle)
        ticket = ParkingTicket(uuid.uuid4(), vehicle, slot, datetime.now(), None)
        self.active_tickets[ticket.ticket_id] = ticket
        print(f"Vehicle Parked Successfully")
        print(f"Ticket ID : {ticket.ticket_id}")
        print(f"Allocated Slot : {slot.slot_id}")
        return ticket
    
    def set_payment_strategy(self, payment_strategy):
        self.payment_strategy = payment_strategy
        
    def unpark_vehicle(self, ticket_id):
        if ticket_id not in self.active_tickets:
            raise Exception("Invalid Ticket")
        ticket = self.active_tickets[ticket_id]
        ticket.slot.unpark_vehicle()
        entry_time = ticket.get_entry_time
        exit_time = ticket.get_exit_time()
        total_time = entry_time - exit_time
        Payment(total_time).make_payment(self.payment_strategy)
        del self.active_tickets[ticket_id]
        print("Vehicle Unparked Successfully")
    
    def get_vehicle_count(self):
        return len(self.active_tickets)
    
    def get_vehicle_count_by_type(self, vehicle_type):
        return sum(1 for ticket in self.active_tickets if ticket.vehicle.vehicle_type == vehicle_type)
    
    

def main():
    parking_lot = ParkingLot(uuid.uuid4(), "Parking Lot 1", "123 Main St", FirstAvailableParkingStrategy())
    parking_lot.add_slot(ParkingSlot(uuid.uuid4(), ParkingSlotType.SMALL, Floor.ONE, 1, 1))
    parking_lot.add_slot(ParkingSlot(uuid.uuid4(), ParkingSlotType.MEDIUM, Floor.ONE, 1, 2))
    parking_lot.add_slot(ParkingSlot(uuid.uuid4(), ParkingSlotType.LARGE, Floor.ONE, 1, 3))
    parking_lot.add_slot(ParkingSlot(uuid.uuid4(), ParkingSlotType.SMALL, Floor.TWO, 1, 1))
    parking_lot.add_slot(ParkingSlot(uuid.uuid4(), ParkingSlotType.MEDIUM, Floor.TWO, 1, 2))
    parking_lot.add_slot(ParkingSlot(uuid.uuid4(), ParkingSlotType.LARGE, Floor.TWO, 1, 3))
    parking_lot.add_slot(ParkingSlot(uuid.uuid4(), ParkingSlotType.SMALL, Floor.THREE, 1, 1))
    parking_lot.add_slot(ParkingSlot(uuid.uuid4(), ParkingSlotType.MEDIUM, Floor.THREE, 1, 2))
    parking_lot.add_slot(ParkingSlot(uuid.uuid4(), ParkingSlotType.LARGE, Floor.THREE, 1, 3))
    
    
    ## park in 
    vehicle = Vehicle("ABC-123", VehicleType.SMALL)
    ticket = parking_lot.park_vehicle(vehicle)
    print(ticket)
    
    ## unpark in
    parking_lot.unpark_vehicle(ticket.ticket_id)
    print(ticket)
    

