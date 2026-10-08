from patterns.behavioral.order_mediator import (
    FoodOrderMediator,
    Customer,
    Restaurant,
    DeliveryPartner
)


mediator = FoodOrderMediator()


customer = Customer(mediator)
restaurant = Restaurant(mediator)
delivery_partner = DeliveryPartner(mediator)


mediator.set_customer(customer)
mediator.set_restaurant(restaurant)
mediator.set_delivery_partner(delivery_partner)


print("Customer sends message:")

messages = customer.send_message(
    "I placed order #1"
)

for message in messages:
    print(message)


print("\nRestaurant sends message:")

messages = restaurant.send_message(
    "Order #1 is ready"
)

for message in messages:
    print(message)


print("\nDelivery Partner sends message:")

messages = delivery_partner.send_message(
    "Order #1 has been delivered"
)

for message in messages:
    print(message)