from abc import ABC, abstractmethod


class OrderElement(ABC):

    @abstractmethod
    def accept(self, visitor):
        pass


class FoodItem(OrderElement):

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def accept(self, visitor):
        return visitor.visit_food_item(self)


class DeliveryItem(OrderElement):

    def __init__(self, distance):
        self.distance = distance

    def accept(self, visitor):
        return visitor.visit_delivery_item(self)


class OrderReportVisitor:

    def visit_food_item(self, food_item):

        total = (
            food_item.price *
            food_item.quantity
        )

        return (
            f"{food_item.name}: "
            f"{food_item.quantity} × "
            f"₹{food_item.price} = ₹{total}"
        )

    def visit_delivery_item(self, delivery_item):

        return (
            f"Delivery distance: "
            f"{delivery_item.distance} km"
        )


class OrderTotalVisitor:

    def __init__(self):
        self.total = 0

    def visit_food_item(self, food_item):

        self.total += (
            food_item.price *
            food_item.quantity
        )

    def visit_delivery_item(self, delivery_item):

        if delivery_item.distance <= 3:
            self.total += 30

        elif delivery_item.distance <= 7:
            self.total += 50

        else:
            self.total += 70

    def get_total(self):
        return self.total