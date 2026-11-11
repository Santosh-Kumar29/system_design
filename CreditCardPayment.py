## FactoryDesignPattern
#CreditCardPayment

from abc import ABC, abstractmethod

class PaymentFactory(ABC):
    @abstractmethod
    def create_payment_method(self) -> None:
        raise NotImplementedError("Payment method not implemented")

class CreditCardPaymentFactory(PaymentFactory):
    def create_payment_method(self) -> None:
        print("Credit card payment created")

class DebitCardPaymentFactory(PaymentFactory):
    def create_payment_method(self) -> None:
        print("Debit card payment created")
    
    
    
class PaymentFactory:
    def create_payment_method(self, payment_method: CreditCardPaymentFactory | DebitCardPaymentFactory) -> PaymentFactory:
        if isinstance(payment_method, CreditCardPaymentFactory):
            return CreditCardPaymentFactory()
        elif isinstance(payment_method, DebitCardPaymentFactory):
            return DebitCardPaymentFactory()
        else:
            raise ValueError("Invalid payment method")


## pay
PaymentFactory().create_payment_method(DebitCardPaymentFactory()).create_payment_method()