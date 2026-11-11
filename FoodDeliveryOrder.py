# Placed
# Preparing
# OutForDelivery
# Delivered
# Cancelled


from abc import ABC, abstractmethod



class OrderState(ABC):
    
    # @abstractmethod
    # def initial_state(self):
    #     pass

    @abstractmethod
    def placed_state(self):
        pass

    @abstractmethod
    def prepare_state(self):
        pass

    @abstractmethod
    def prepared_state(self):
        pass
    
    @abstractmethod
    def out_for_delivery_state(self):
        pass

    @abstractmethod
    def delivered_state(self):
        pass

    @abstractmethod
    def cancelled_state(self):
        pass
    
class InitialState(OrderState):

    def placed_state(self):
        print("Order is placed")
        return PlacedState()

    def prepare_state(self):
        print("Order is not placed yet")
        return self
    
    def prepared_state(self):
        print("Order is not prepared yet")
        return self
    
    def out_for_delivery_state(self):
        print("Order is not placed yet")
        return self
    def delivered_state(self):
        print("Order is not placed yet")
        return self
    def cancelled_state(self):
        print("Order is cancelled")
        return CancelledState()
        
class PlacedState(OrderState):
    # def initial_state(self):
    #     print("Order is placed")
    #     return self

    def placed_state(self):
        print("Order is already placed")
        return self

    def prepare_state(self):
        print("Order is preparing")
        return PrepareState()

    def prepared_state(self):
        print("Order is prepared")
        return self
    
    def out_for_delivery_state(self):
        print("Order is not prepared yet")
        return self

    def delivered_state(self):
        print("Order is not prepared yet")
        return self

    def cancelled_state(self):
        print("Order is cancellled")
        return CancelledState()

class PrepareState(OrderState):
    # def initial_state(self):
    #     print("Order is preparing")
    #     return self
    
    def placed_state(self):
        print("Order is already placed")
        return self
    
    def prepare_state(self):
        print("Order is prepared")
        return self
    
    def prepared_state(self):
        print("Order is prepared")
        return OutForDeliveryState()
    
    def out_for_delivery_state(self):
        print("Order is prepared")
        return self

    def delivered_state(self):
        print("Order is not packed yet")
        return self

    def cancelled_state(self):
        print("Order is cancelled")
        return CancelledState()
        
        
        
class OutForDeliveryState(OrderState):

    def placed_state(self):
        print("Order is already placed")
        return self
    
    def prepare_state(self):
        print("Order is prepared")
        return self

    def prepared_state(self):
        print("Order is prepared")
        return self
    
    def out_for_delivery_state(self):
        print("Order is out for delivery")
        return DeliveredState()

    def delivered_state(self):
        print("Order is not delivered yet")
        return self

    def cancelled_state(self):
        print("Order is can not be cancelled")
        return self
        
        
class DeliveredState(OrderState):

    def placed_state(self):
        print("Order is already placed")
        return self
    
    def prepare_state(self):
        print("Order is already delivered")
        return self

    def prepared_state(self):
        print("Order is already delivered")
        return self

    def out_for_delivery_state(self):
        print("Order is already delivered")
        return self

    def delivered_state(self):
        print("Order is delivered")
        return self
    
    def cancelled_state(self):
        print("Order is already delivered, cannot be cancelled")
        return self
        
        
class CancelledState(OrderState): 
        
    def placed_state(self):
        print("Order is cancelled")
        return self
    
    def prepare_state(self):
        print("Order is cancelled")
        return self

    def prepared_state(self):
        print("Order is cancelled")
        return self

    def out_for_delivery_state(self):
        print("Order is cancelled")
        return self

    def delivered_state(self):
        print("Order is cancelled")
        return self

    def cancelled_state(self):
        print("Order is cancelled")
        return self
        
        
class RestaurantManagemnt:
    
    def __init__(self):
        self.state = InitialState()
        
    def placed_state(self):
        self.state = self.state.placed_state()
        
    def prepare_state(self):
        self.state = self.state.prepare_state()
        
    def prepared_state(self):
        self.state = self.state.prepared_state()
        
    def out_for_delivery_state(self):
        self.state = self.state.out_for_delivery_state()
        
    def delivered_state(self):
        self.state = self.state.delivered_state()
        
    def cancelled_state(self):
        self,state = self.state.cancelled_state()
        
va = RestaurantManagemnt()
va.placed_state()
va.delivered_state()
