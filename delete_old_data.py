from database import get_connection

connection = get_connection()
cursor = connection.cursor()

cursor.execute(
    "DELETE FROM restaurants WHERE id = ?",
    (1,)
)

connection.commit()
connection.close()

print("Old restaurant deleted.")