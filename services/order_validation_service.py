from patterns.behavioral.order_validation_chain import (
    CustomerValidationHandler,
    RestaurantValidationHandler,
    FoodValidationHandler,
    PaymentValidationHandler
)


def validate_order(order):

    customer_handler = CustomerValidationHandler()
    restaurant_handler = RestaurantValidationHandler()
    food_handler = FoodValidationHandler()
    payment_handler = PaymentValidationHandler()

    customer_handler.set_next(
        restaurant_handler
    ).set_next(
        food_handler
    ).set_next(
        payment_handler
    )

    return customer_handler.validate(order)