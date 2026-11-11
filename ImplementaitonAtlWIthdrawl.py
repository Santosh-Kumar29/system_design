from AtmWithdrawl import AtmState, IdleState, CardInsertedState, EnterPin, Withdraw, Reject


## card creation
class Card:
    def __init__(self, card_number, expiry, cvv, pin) -> None:
        self.card_number = card_number
        self.expiry = expiry
        self.cvv = cvv
        self.pin = pin
    
    def create_card(self):
        print("card created")

## bank account creation
class BankAccount:
    def __init__(self, account_number, initial_balance, card: Card) -> None:
        self.account_number = account_number
        self.initial_balance = initial_balance
        self.card  = card
    
    def validate_card_pin(self, inserted_pin):
        return inserted_pin == self.card.pin 
        
    def amount_deduct(self, amount):
        self.initial_balance = self.initial_balance - amount

    def is_enough_balance(self, amount):
        return amount <= self.initial_balance
        

    def deposit(self, amount):
        self.initial_balance += amount
        
    def check_balnce(self):
        return self.initial_balance
        

class AtmState:
    def insert_card(self):
        raise NotImplementedError("Insert method not implemented")
    def insert_pin(self):
        raise NotImplementedError("insert pin not implemented")
    def balance_check(self):
        raise NotImplementedError("balnce check not implemnted")
    def withdrawl_money(self):
        raise NotImplementedError("Withdrawl Money not implemned")
    def release_card(self):
        raise NotImplementedError("Release card not implemented")
    

class InsertCardState(AtmState):
    
    def insert_card(self):
        print("card is inserted")
        return InsertPinState()
    
    def release_card(self):
        print("card is relaeased")
        return ReleseState()
    

class InsertPinState(AtmState):
    def insert_pin(self, pin_number, bank_account: BankAccount):
        if bank_account.validate_card_pin(pin_number):
            choice = int(input("pin verified, please choose from below option \n Enter 1. For balance check \nEnter 2 for cash Withdrawl"))
            if choice == 1:
                return BalanceeCheckState()
            elif choice == 2:
                return CashWithdrawlState()
            else:
                print("invalid choice")
                return ReleseState()
        else:
            print("invalid Pin")
            return ReleseState()
        
        
        
class BalanceeCheckState(AtmState):
    def balance_check(self, bank: BankAccount):
        print(bank.check_balnce())
        return ReleseState()
    

class CashWithdrawlState(AtmState):
    def withdrawl_money(self, bank: BankAccount, amount, note_combination):
        if bank.is_enough_balance(amount):
            bank.amount_deduct()
            print(note_combination)
            return ReleseState()
        else:
            print("You dont have a enough balance: garib aadmi")
            return ReleseState()
            
        
    
class ReleseState(AtmState):
    def release_card(self):
        print("card released")
        return self

     

        
class AtmMachine:
    
    noteDic = {2000 : 100 , 500: 30,  100: 500,  50: 400, 20: 600 , 10: 550}        
        
    def __init__(self, bank: BankAccount) -> None:
        self.bank = bank
        self.state = InsertCardState()
        
    @classmethod
    def note_combination_checker(cls, amount):
        sortedNote = dict(sorted(cls.noteDic.items(), reverse=True))
        note_dic = {}
        for key, val in sortedNote.items():
            rem = amount%key
            take_note = int(min((amount - rem) / key, val))
            if rem == 0 and take_note * key == amount:
                note_dic[key] = take_note
                cls.noteDic[key] -= take_note
                return note_dic
            else:
                if take_note:
                    note_dic[key] = take_note
                    cls.noteDic[key] -= take_note
                    amount = amount - take_note * key
        return False
    
    def insert_card(self):
        self.state = self.state.insert_card()
        
    def insert_pin(self, pin_number):
        self.state = self.state.insert_pin(pin_number, self.bank)
        
    def check_balance(self):
        self.state = self.state.balance_check(self.bank)
        
    def withdrawl_money(self, amount):
        note_combination_checker = self.note_combination_checker(amount)
        if note_combination_checker:
            self.state = self.state.withdrawl_money(self.bank, amount, self.note_combination_checker)
        else:
            print("No Such Combination Found")
            self.state = ReleseState()
    def release_state(self):
        self.state = self.state.release_card()
        
    