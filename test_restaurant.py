import requests

url = "http://127.0.0.1:5000/restaurants"

data = {
    "name": "Amma Mess",
    "location": "Tallakulam, Madurai",
    "rating": 4.5
}

response = requests.post(url, json=data)

print("Status:", response.status_code)
print("Response:", response.json())