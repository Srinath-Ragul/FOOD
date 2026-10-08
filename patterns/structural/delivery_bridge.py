from abc import ABC, abstractmethod


class NotificationChannel(ABC):

    @abstractmethod
    def send(self, message):
        pass


class SMSNotification(NotificationChannel):

    def send(self, message):
        return f"SMS: {message}"


class EmailNotification(NotificationChannel):

    def send(self, message):
        return f"Email: {message}"


class DeliveryService(ABC):

    def __init__(self, notification_channel):
        self.notification_channel = notification_channel

    @abstractmethod
    def update_delivery(self, order_id):
        pass


class NormalDeliveryService(DeliveryService):

    def update_delivery(self, order_id):

        message = (
            f"Normal delivery update for order #{order_id}"
        )

        return self.notification_channel.send(message)


class ExpressDeliveryService(DeliveryService):

    def update_delivery(self, order_id):

        message = (
            f"Express delivery update for order #{order_id}"
        )

        return self.notification_channel.send(message)