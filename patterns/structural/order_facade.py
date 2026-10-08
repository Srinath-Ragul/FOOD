from patterns.creational.order_factory import OrderFactory
from patterns.creational.order_builder import OrderBuilder
from services.delivery_service import calculate_delivery_charge
from services.payment_service import process_payment
from database import get_connection


class OrderFacade:

    def place_order(
        self,
        customer_id,
        restaurant_id,
        order_type,
        items,
        delivery_type,
        distance,
        payment_method
    ):

        # 1. Factory Pattern
        order_object = OrderFactory.create_order(
            order_type
        )

        # 2. Builder Pattern
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

        # 3. Strategy Pattern
        delivery_charge = calculate_delivery_charge(
            delivery_type,
            distance
        )

        final_amount = (
            order_data["total_amount"]
            + delivery_charge
        )

        # 4. Save order to database
        connection = get_connection()
        cursor = connection.cursor()

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
            customer_id,
            restaurant_id,
            final_amount,
            "PLACED"
        ))

        order_id = cursor.lastrowid

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

        # 5. Payment through Adapter
        payment_result = process_payment(
            order_id,
            payment_method,
            final_amount
        )

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
            "payment": payment_result,
            "status": "PLACED"
        }