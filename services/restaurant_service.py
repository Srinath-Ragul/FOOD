from database import get_connection


def get_all_restaurants():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, location, rating
        FROM restaurants
    """)

    rows = cursor.fetchall()

    connection.close()

    restaurants = []

    for row in rows:
        restaurants.append({
            "id": row["id"],
            "name": row["name"],
            "location": row["location"],
            "rating": row["rating"]
        })

    return restaurants


def add_restaurant(name, location, rating):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO restaurants (name, location, rating)
        VALUES (?, ?, ?)
    """, (name, location, rating))

    connection.commit()

    restaurant_id = cursor.lastrowid

    connection.close()

    return restaurant_id