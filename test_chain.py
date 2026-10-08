from services.order_validation_service import validate_order


valid_order = {
    "customer_id": 1,
    "restaurant_id": 2,
    "payment_method": "upi",
    "items": [
        {
            "food_id": 1,
            "quantity": 2
        }
    ]
}


print("Valid Order:")
print(validate_order(valid_order))


invalid_order = {
    "customer_id": 1,
    "restaurant_id": 2,
    "payment_method": "upi",
    "items": []
}


print("\nInvalid Order:")
print(validate_order(invalid_order))