# ATM Machine
# Idle
# CardInserted
# PinVerified
# CashDispensed

# operation:
# insert_card()
# enter_pin()
# withdraw()
# eject_card()

# rules:
# Can't withdraw before PIN verification.
# Can't insert two cards.
# After dispensing cash, ATM returns to Idle.

from abc import ABC, abstractmethod
class AtmState(ABC):
    
    @abstractmethod
    def insert_card(self):
        pass
    @abstractmethod
    def enter_pin(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass
    @abstractmethod
    def reject_card(self):
        pass
    
class IdleState(AtmState):
    
    def insert_card(self):
        print("Card inserted")
        return CardInsertedState()
    
    def enter_pin(self):
        print("Can't enter PIN before card is inserted")
        return self
    def withdraw(self):
        print("Can't withdraw before PIN is verified")
        return self
    def reject_card(self):
        print("Can't reject card in Idle state")
        return self
    
class CardInsertedState(AtmState):
    def insert_card(self):
        print("card already inserted")
        return self
        
    def enter_pin(self):
        print("pin entering")
        return EnterPin()

    def withdraw(self):
        print("you can withraw without enter pin")
        return self

    def reject_card(self):
        print("please enter the pin")
        return self

class EnterPin(AtmState):
    def insert_card(self):
        print("card already inserted")
        return self

    def enter_pin(self):
        print("pin already entered")
        return self
    
    def withdraw(self):
        print("withdraw is under process")
        return Withdraw()
    
    def reject_card(self):
        print("card rejected")
        return Reject()
    
    
class Withdraw(AtmState):
    def insert_card(self):
        print("card already inserted")
        return self

    def enter_pin(self):
        print("pin already entered, you can not enter again")
        return self
    
    def withdraw(self):
        print("amount wthdraw successfully")
        return self
    def reject_card(self):
        print("card  can not be rejected")
        return self
    
    
class Reject(AtmState):
    def insert_card(self):
        print("card already inserted")
        return self
    def enter_pin(self):
        print("pin already entered")
        return self
    def withdraw(self):
        print("amount wthdraw successfully")
        return self
    def reject_card(self):
        print("card rejected")
        return self
    
# class Atm:
#     def __init__(self):
#         self.state = IdleState()
#     def insert_card(self):
#         self.state = self.state.insert_card()
#     def enter_pin(self):
#         self.state = self.state.enter_pin()
#     def withdraw(self):
#         self.state = self.state.withdraw()
#     def reject_card(self):
#         self.state = self.state.reject_card()
        
# test_case = Atm()
# test_case.insert_card()
# test_case.withdraw()
# test_case.enter_pin()

# test_case.reject_card()