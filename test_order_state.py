import requests


order_id = 1

base_url = f"http://127.0.0.1:5000/orders/{order_id}"


response = requests.get(
    f"{base_url}/status"
)

print("Current status:")
print(response.json())


print("\nMoving to next state...")

response = requests.put(
    f"{base_url}/next"
)

result = response.json()

print(result)


print("\nNotifications:")

if "notifications" in result:

    for notification in result["notifications"]:
        print(notification)


print("\nChecking status again...")

response = requests.get(
    f"{base_url}/status"
)

print(response.json())