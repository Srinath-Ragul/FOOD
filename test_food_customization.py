import requests


url = "http://127.0.0.1:5000/food/customize"


data = {
    "name": "Chicken Biryani",
    "price": 180,
    "extras": [
        "extra_egg",
        "extra_chicken"
    ]
}


response = requests.post(
    url,
    json=data
)


print("Status:", response.status_code)

print("Customization Response:")

print(response.json())