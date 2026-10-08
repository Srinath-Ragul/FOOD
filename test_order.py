import requests


url = "http://127.0.0.1:5000/orders"


data = {

    "customer_id": 1,

    "restaurant_id": 2,

    "order_type": "normal",

    "delivery_type": "express",

    "distance": 5,

    "items": [

        {
            "food_id": 1,
            "quantity": 2,
            "price": 120
        },

        {
            "food_id": 2,
            "quantity": 3,
            "price": 40
        }

    ]
}


response = requests.post(
    url,
    json=data
)


print("Status:", response.status_code)

print("Response:")

print(response.json())