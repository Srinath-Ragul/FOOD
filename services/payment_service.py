from database import get_connection

from patterns.structural.payment_adapter import (
    UPIAdapter,
    CardAdapter
)


def process_payment(order_id, payment_method, amount):

    if payment_method == "upi":
        payment_processor = UPIAdapter()

    elif payment_method == "card":
        payment_processor = CardAdapter()

    else:
        raise ValueError(
            "Invalid payment method. Use upi or card."
        )

    payment_result = payment_processor.process_payment(
        amount
    )

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO payments
        (
            order_id,
            payment_method,
            amount,
            status
        )
        VALUES (?, ?, ?, ?)
    """, (
        order_id,
        payment_method,
        amount,
        payment_result["status"]
    ))

    connection.commit()

    payment_id = cursor.lastrowid

    connection.close()

    return {
        "payment_id": payment_id,
        "order_id": order_id,
        "payment_method": payment_method,
        "amount": amount,
        "status": payment_result["status"],
        "transaction_id": payment_result["transaction_id"]
    }