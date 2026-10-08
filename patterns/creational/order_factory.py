from abc import ABC, abstractmethod


# Product
class Order(ABC):

    @abstractmethod
    def create_order(self, customer_id, restaurant_id, items):
        pass


# Concrete Product 1
class NormalOrder(Order):

    def create_order(self, customer_id, restaurant_id, items):

        return {
            "type": "Normal Order",
            "customer_id": customer_id,
            "restaurant_id": restaurant_id,
            "items": items
        }


# Concrete Product 2
class BulkOrder(Order):

    def create_order(self, customer_id, restaurant_id, items):

        return {
            "type": "Bulk Order",
            "customer_id": customer_id,
            "restaurant_id": restaurant_id,
            "items": items
        }


# Concrete Product 3
class PreOrder(Order):

    def create_order(self, customer_id, restaurant_id, items):

        return {
            "type": "Pre Order",
            "customer_id": customer_id,
            "restaurant_id": restaurant_id,
            "items": items
        }


# Factory
class OrderFactory:

    @staticmethod
    def create_order(order_type):

        if order_type == "normal":
            return NormalOrder()

        elif order_type == "bulk":
            return BulkOrder()

        elif order_type == "preorder":
            return PreOrder()

        else:
            raise ValueError("Invalid order type")