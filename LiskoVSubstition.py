## liskov subsctitution



import abc

from abc import ABC, abstractmethod

    
class CreditAccount(ABC):
    @abstractmethod
    def create_credit_account(self) -> None:
        print("Credit account created")
        
class DebitAccount(ABC):
    @abstractmethod
    def create_debit_account(self) -> None:
        print("Debit account created")
        
        
class SavingsAccount(CreditAccount, DebitAccount):
    def create_credit_account(self) -> None:
        print("Savings account created")
    def create_debit_account(self) -> None:
        print("Savings account created")
        
class CheckingAccount(CreditAccount, DebitAccount):
    def create_credit_account(self) -> None:
        print("Checking account created")
    def create_debit_account(self) -> None:
        print("Checking account created")
    
    
class FDAccount(CreditAccount):
    def create_credit_account(self) -> None:
        print("FD account created")
        
