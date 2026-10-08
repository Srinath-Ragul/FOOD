import requests


url = "http://127.0.0.1:5000/orders/place"


data = {
    "customer_id": 1,
    "restaurant_id": 2,
    "order_type": "normal",
    "delivery_type": "express",
    "distance": 5,
    "payment_method": "upi",
    "items": [
        {
            "food_id": 1,
            "quantity": 1,
            "price": 120
        },
        {
            "food_id": 2,
            "quantity": 2,
            "price": 40
        }
    ]
}


response = requests.post(
    url,
    json=data
)


print("Status:", response.status_code)

print("\nOrder Response:")

print(response.json())