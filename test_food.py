import requests

restaurant_id = 2

url = f"http://127.0.0.1:5000/restaurants/{restaurant_id}/foods"

foods = [
    {
        "name": "Kari Dosa",
        "price": 120,
        "category": "South Indian"
    },
    {
        "name": "Parotta",
        "price": 40,
        "category": "Main Course"
    },
    {
        "name": "Chicken Biryani",
        "price": 180,
        "category": "Biryani"
    },
    {
        "name": "Fish Curry",
        "price": 150,
        "category": "Non-Veg"
    }
]

for food in foods:

    response = requests.post(
        url,
        json=food
    )

    print(response.status_code)
    print(response.json())