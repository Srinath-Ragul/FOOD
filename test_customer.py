import requests

url = "http://127.0.0.1:5000/customers"

data = {
    "name": "Srinath",
    "email": "srinath@gmail.com",
    "password": "12345"
}

response = requests.post(url, json=data)

print("Status:", response.status_code)
print("Response:", response.json())