from database import get_connection


def get_all_customers():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, email
        FROM users
        WHERE role = 'customer'
    """)

    rows = cursor.fetchall()

    connection.close()

    customers = []

    for row in rows:
        customers.append({
            "id": row["id"],
            "name": row["name"],
            "email": row["email"]
        })

    return customers


def add_customer(name, email, password):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO users (name, email, password, role)
        VALUES (?, ?, ?, ?)
    """, (name, email, password, "customer"))

    connection.commit()

    customer_id = cursor.lastrowid

    connection.close()

    return customer_id