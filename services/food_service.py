from database import get_connection


def get_food_by_restaurant(restaurant_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, restaurant_id, name, price, category, availability
        FROM food_items
        WHERE restaurant_id = ?
    """, (restaurant_id,))

    rows = cursor.fetchall()
    connection.close()

    foods = []

    for row in rows:
        foods.append({
            "id": row["id"],
            "restaurant_id": row["restaurant_id"],
            "name": row["name"],
            "price": row["price"],
            "category": row["category"],
            "availability": row["availability"]
        })

    return foods


def add_food(restaurant_id, name, price, category):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO food_items
        (restaurant_id, name, price, category)
        VALUES (?, ?, ?, ?)
    """, (restaurant_id, name, price, category))

    connection.commit()

    food_id = cursor.lastrowid

    connection.close()

    return food_id