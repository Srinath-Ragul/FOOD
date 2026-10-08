from database import get_connection


def get_all_orders():

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute("""
        SELECT
            o.id,
            o.customer_id,
            u.name AS customer_name,
            o.restaurant_id,
            r.name AS restaurant_name,
            o.total_amount,
            o.status,
            o.created_at
        FROM orders o

        LEFT JOIN users u
            ON o.customer_id = u.id

        LEFT JOIN restaurants r
            ON o.restaurant_id = r.id

        ORDER BY o.id DESC
    """)


    rows = cursor.fetchall()

    connection.close()


    orders = []


    for row in rows:

        orders.append({

            "id":
                row["id"],

            "customer_id":
                row["customer_id"],

            "customer_name":
                row["customer_name"],

            "restaurant_id":
                row["restaurant_id"],

            "restaurant_name":
                row["restaurant_name"],

            "total_amount":
                row["total_amount"],

            "status":
                row["status"],

            "created_at":
                row["created_at"]

        })


    return orders