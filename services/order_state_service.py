from database import get_connection

from patterns.behavioral.order_state import OrderStateManager

from patterns.behavioral.order_observer import (
    OrderSubject,
    CustomerObserver,
    RestaurantObserver,
    DeliveryPartnerObserver
)


def get_order_status(order_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT status
        FROM orders
        WHERE id = ?
    """, (order_id,))

    row = cursor.fetchone()

    connection.close()

    if row is None:
        return None

    return row["status"]


def update_order_status(order_id, new_status):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE orders
        SET status = ?
        WHERE id = ?
    """, (
        new_status,
        order_id
    ))

    connection.commit()
    connection.close()


def move_order_to_next_state(order_id):

    current_status = get_order_status(order_id)

    if current_status is None:
        return {
            "error": "Order not found"
        }

    state_manager = OrderStateManager()

    while state_manager.get_status() != current_status:

        previous_status = state_manager.get_status()

        state_manager.move_to_next_state()

        if state_manager.get_status() == previous_status:
            return {
                "error": "Invalid order state"
            }

    state_manager.move_to_next_state()

    new_status = state_manager.get_status()

    update_order_status(
        order_id,
        new_status
    )

    # Create Observer Subject
    order_subject = OrderSubject()

    # Create Observers
    customer_observer = CustomerObserver()
    restaurant_observer = RestaurantObserver()
    delivery_observer = DeliveryPartnerObserver()

    # Attach observers
    order_subject.attach(customer_observer)
    order_subject.attach(restaurant_observer)
    order_subject.attach(delivery_observer)

    # Notify all observers
    notifications = order_subject.notify(
        order_id,
        new_status
    )

    return {
        "order_id": order_id,
        "previous_status": current_status,
        "new_status": new_status,
        "notifications": notifications
    }