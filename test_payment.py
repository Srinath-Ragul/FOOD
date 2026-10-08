import requests


url = "http://127.0.0.1:5000/payments"


data = {
    "order_id": 1,
    "payment_method": "upi",
    "amount": 430
}


response = requests.post(
    url,
    json=data
)


print("Status:", response.status_code)

print("Payment Response:")

print(response.json())