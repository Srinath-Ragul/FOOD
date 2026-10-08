from abc import ABC, abstractmethod


class OrderState(ABC):

    @abstractmethod
    def next_state(self, order):
        pass

    @abstractmethod
    def get_status(self):
        pass


class PlacedState(OrderState):

    def next_state(self, order):
        order.state = AcceptedState()

    def get_status(self):
        return "PLACED"


class AcceptedState(OrderState):

    def next_state(self, order):
        order.state = PreparingState()

    def get_status(self):
        return "ACCEPTED"


class PreparingState(OrderState):

    def next_state(self, order):
        order.state = ReadyState()

    def get_status(self):
        return "PREPARING"


class ReadyState(OrderState):

    def next_state(self, order):
        order.state = OutForDeliveryState()

    def get_status(self):
        return "READY"


class OutForDeliveryState(OrderState):

    def next_state(self, order):
        order.state = DeliveredState()

    def get_status(self):
        return "OUT_FOR_DELIVERY"


class DeliveredState(OrderState):

    def next_state(self, order):
        print("Order is already delivered.")

    def get_status(self):
        return "DELIVERED"


class OrderStateManager:

    def __init__(self):
        self.state = PlacedState()

    def move_to_next_state(self):
        self.state.next_state(self)

    def get_status(self):
        return self.state.get_status()