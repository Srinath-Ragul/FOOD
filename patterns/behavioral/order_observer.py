from abc import ABC, abstractmethod


class OrderObserver(ABC):

    @abstractmethod
    def update(self, order_id, status):
        pass


class CustomerObserver(OrderObserver):

    def update(self, order_id, status):
        return (
            f"Customer: Your order #{order_id} "
            f"has been {status}."
        )


class RestaurantObserver(OrderObserver):

    def update(self, order_id, status):
        return (
            f"Restaurant: Order #{order_id} "
            f"has been {status}."
        )


class DeliveryPartnerObserver(OrderObserver):

    def update(self, order_id, status):
        return (
            f"Delivery Partner: Order #{order_id} "
            f"is now {status}."
        )


class OrderSubject:

    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify(self, order_id, status):

        notifications = []

        for observer in self.observers:
            message = observer.update(
                order_id,
                status
            )

            notifications.append(message)

        return notifications