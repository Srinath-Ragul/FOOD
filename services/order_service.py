from database import get_connection

from patterns.creational.order_factory import OrderFactory
from patterns.creational.order_builder import OrderBuilder

from services.delivery_service import calculate_delivery_charge


def create_order(
    customer_id,
    restaurant_id,
    order_type,
    items,
    delivery_type,
    distance
):

    # Factory Method
    order_object = OrderFactory.create_order(order_type)

    # Builder Pattern
    builder = OrderBuilder()

    builder.set_customer(customer_id)
    builder.set_restaurant(restaurant_id)
    builder.set_order_type(order_type)

    for item in items:

        builder.add_item(
            item["food_id"],
            item["quantity"],
            item["price"]
        )

    builder.set_status("PLACED")

    order_data = builder.build()

    # Strategy Pattern
    delivery_charge = calculate_delivery_charge(
        delivery_type,
        distance
    )

    # Final amount
    final_amount = (
        order_data["total_amount"] +
        delivery_charge
    )

    # Database connection
    connection = get_connection()
    cursor = connection.cursor()

    # Insert order
    cursor.execute("""
        INSERT INTO orders
        (
            customer_id,
            restaurant_id,
            total_amount,
            status
        )
        VALUES (?, ?, ?, ?)
    """, (
        order_data["customer_id"],
        order_data["restaurant_id"],
        final_amount,
        order_data["status"]
    ))

    order_id = cursor.lastrowid

    # Insert order items
    for item in order_data["items"]:

        cursor.execute("""
            INSERT INTO order_items
            (
                order_id,
                food_id,
                quantity,
                price
            )
            VALUES (?, ?, ?, ?)
        """, (
            order_id,
            item["food_id"],
            item["quantity"],
            item["price"]
        ))

    connection.commit()
    connection.close()

    # Return complete order information
    return {
        "order_id": order_id,

        "order_type": order_object.create_order(
            customer_id,
            restaurant_id,
            items
        )["type"],

        "customer_id": customer_id,

        "restaurant_id": restaurant_id,

        "food_amount": order_data["total_amount"],

        "delivery_type": delivery_type,

        "distance_km": distance,

        "delivery_charge": delivery_charge,

        "total_amount": final_amount,

        "status": order_data["status"]
    }