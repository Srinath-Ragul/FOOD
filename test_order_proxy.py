import requests


order_id = 1


# Customer 1 trying to access order 1
url = (
    f"http://127.0.0.1:5000"
    f"/orders/{order_id}/secure"
    f"?customer_id=1"
)


response = requests.get(url)

print("Customer 1:")
print(response.status_code)
print(response.json())


# Customer 2 trying to access order 1
url = (
    f"http://127.0.0.1:5000"
    f"/orders/{order_id}/secure"
    f"?customer_id=2"
)


response = requests.get(url)

print("\nCustomer 2:")
print(response.status_code)
print(response.json())