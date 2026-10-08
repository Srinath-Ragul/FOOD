from patterns.creational.database_singleton import (
    DatabaseManager
)


database1 = DatabaseManager()
database2 = DatabaseManager()


print("Database 1:", id(database1))
print("Database 2:", id(database2))


if database1 is database2:
    print("Singleton working successfully!")
else:
    print("Singleton failed!")