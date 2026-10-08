from database import get_connection


class OrderService:

    def get_order(self, order_id):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, customer_id, restaurant_id,
                   total_amount, status
            FROM orders
            WHERE id = ?
        """, (order_id,))

        row = cursor.fetchone()
        connection.close()

        if row is None:
            return None

        return {
            "order_id": row["id"],
            "customer_id": row["customer_id"],
            "restaurant_id": row["restaurant_id"],
            "total_amount": row["total_amount"],
            "status": row["status"]
        }


class OrderProxy:

    def __init__(self):
        self.order_service = OrderService()

    def get_order(self, order_id, customer_id):

        order = self.order_service.get_order(order_id)

        if order is None:
            return {
                "error": "Order not found"
            }

        if order["customer_id"] != customer_id:
            return {
                "error": "Access denied"
            }

        return order