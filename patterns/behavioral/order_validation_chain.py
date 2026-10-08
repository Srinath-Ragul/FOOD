from abc import ABC, abstractmethod


class OrderValidationHandler(ABC):

    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler

    @abstractmethod
    def validate(self, order):
        pass

    def pass_to_next(self, order):

        if self.next_handler:
            return self.next_handler.validate(order)

        return {
            "valid": True,
            "message": "Order validation successful"
        }


class CustomerValidationHandler(OrderValidationHandler):

    def validate(self, order):

        if order.get("customer_id") is None:
            return {
                "valid": False,
                "message": "Customer ID is required"
            }

        return self.pass_to_next(order)


class RestaurantValidationHandler(OrderValidationHandler):

    def validate(self, order):

        if order.get("restaurant_id") is None:
            return {
                "valid": False,
                "message": "Restaurant ID is required"
            }

        return self.pass_to_next(order)


class FoodValidationHandler(OrderValidationHandler):

    def validate(self, order):

        items = order.get("items", [])

        if not items:
            return {
                "valid": False,
                "message": "Order must contain at least one food item"
            }

        for item in items:

            if item.get("food_id") is None:
                return {
                    "valid": False,
                    "message": "Food ID is required"
                }

            if item.get("quantity", 0) <= 0:
                return {
                    "valid": False,
                    "message": "Food quantity must be greater than zero"
                }

        return self.pass_to_next(order)


class PaymentValidationHandler(OrderValidationHandler):

    def validate(self, order):

        payment_method = order.get("payment_method")

        if payment_method not in ["upi", "card"]:
            return {
                "valid": False,
                "message": "Invalid payment method"
            }

        return self.pass_to_next(order)