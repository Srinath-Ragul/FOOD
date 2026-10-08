from abc import ABC, abstractmethod


class OrderMediator(ABC):

    @abstractmethod
    def send(self, message, sender):
        pass


class Customer:

    def __init__(self, mediator):
        self.mediator = mediator

    def send_message(self, message):
        return self.mediator.send(
            message,
            self
        )

    def receive_message(self, message):
        return f"Customer received: {message}"


class Restaurant:

    def __init__(self, mediator):
        self.mediator = mediator

    def send_message(self, message):
        return self.mediator.send(
            message,
            self
        )

    def receive_message(self, message):
        return f"Restaurant received: {message}"


class DeliveryPartner:

    def __init__(self, mediator):
        self.mediator = mediator

    def send_message(self, message):
        return self.mediator.send(
            message,
            self
        )

    def receive_message(self, message):
        return f"Delivery Partner received: {message}"


class FoodOrderMediator(OrderMediator):

    def __init__(self):

        self.customer = None
        self.restaurant = None
        self.delivery_partner = None

    def set_customer(self, customer):
        self.customer = customer

    def set_restaurant(self, restaurant):
        self.restaurant = restaurant

    def set_delivery_partner(self, delivery_partner):
        self.delivery_partner = delivery_partner

    def send(self, message, sender):

        messages = []

        if sender == self.customer:

            if self.restaurant:
                messages.append(
                    self.restaurant.receive_message(
                        message
                    )
                )

            if self.delivery_partner:
                messages.append(
                    self.delivery_partner.receive_message(
                        message
                    )
                )

        elif sender == self.restaurant:

            if self.customer:
                messages.append(
                    self.customer.receive_message(
                        message
                    )
                )

            if self.delivery_partner:
                messages.append(
                    self.delivery_partner.receive_message(
                        message
                    )
                )

        elif sender == self.delivery_partner:

            if self.customer:
                messages.append(
                    self.customer.receive_message(
                        message
                    )
                )

            if self.restaurant:
                messages.append(
                    self.restaurant.receive_message(
                        message
                    )
                )

        return messages