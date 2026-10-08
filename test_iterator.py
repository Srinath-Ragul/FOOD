from patterns.behavioral.order_iterator import (
    OrderItemCollection
)


items = [
    {
        "food_id": 1,
        "name": "Chicken Biryani",
        "quantity": 2,
        "price": 180
    },
    {
        "food_id": 2,
        "name": "Parotta",
        "quantity": 3,
        "price": 40
    },
    {
        "food_id": 3,
        "name": "Fish Curry",
        "quantity": 1,
        "price": 150
    }
]


collection = OrderItemCollection(items)

iterator = collection.create_iterator()


print("Order Items:")

while iterator.has_next():

    item = iterator.next()

    print(
        f"{item['name']} | "
        f"Quantity: {item['quantity']} | "
        f"Price: ₹{item['price']}"
    )