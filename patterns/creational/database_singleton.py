import sqlite3


class DatabaseManager:

    _instance = None

    def __new__(cls):

        if cls._instance is None:
            cls._instance = super(DatabaseManager, cls).__new__(cls)

        return cls._instance

    def get_connection(self):

        connection = sqlite3.connect(
            "food_ordering.db"
        )

        connection.row_factory = sqlite3.Row

        return connection