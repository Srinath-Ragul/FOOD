from abc import ABC, abstractmethod

from database import get_connection


class OrderCommand(ABC):

    @abstractmethod
    def execute(self):
        pass


class AcceptOrderCommand(OrderCommand):

    def __init__(self, order_id):
        self.order_id = order_id

    def execute(self):

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE orders
            SET status = ?
            WHERE id = ?
        """, (
            "ACCEPTED",
            self.order_id
        ))

        connection.commit()
        connection.close()

        return {
            "order_id": self.order_id,
            "action": "ACCEPT",
            "status": "ACCEPTED"
        }


class PrepareOrderCommand(OrderCommand):

    def __init__(self, order_id):
        self.order_id = order_id

    def execute(self):

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE orders
            SET status = ?
            WHERE id = ?
        """, (
            "PREPARING",
            self.order_id
        ))

        connection.commit()
        connection.close()

        return {
            "order_id": self.order_id,
            "action": "PREPARE",
            "status": "PREPARING"
        }


class CancelOrderCommand(OrderCommand):

    def __init__(self, order_id):
        self.order_id = order_id

    def execute(self):

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE orders
            SET status = ?
            WHERE id = ?
        """, (
            "CANCELLED",
            self.order_id
        ))

        connection.commit()
        connection.close()

        return {
            "order_id": self.order_id,
            "action": "CANCEL",
            "status": "CANCELLED"
        }


class OrderInvoker:

    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def execute_command(self):

        if self.command is None:
            return {
                "error": "No command selected"
            }

        return self.command.execute()