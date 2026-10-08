class OrderBuilder:

    def __init__(self):
        self.order = {
            "customer_id": None,
            "restaurant_id": None,
            "order_type": None,
            "items": [],
            "total_amount": 0,
            "status": "PLACED"
        }

    def set_customer(self, customer_id):
        self.order["customer_id"] = customer_id
        return self

    def set_restaurant(self, restaurant_id):
        self.order["restaurant_id"] = restaurant_id
        return self

    def set_order_type(self, order_type):
        self.order["order_type"] = order_type
        return self

    def add_item(self, food_id, quantity, price):
        self.order["items"].append({
            "food_id": food_id,
            "quantity": quantity,
            "price": price
        })

        self.order["total_amount"] += quantity * price

        return self

    def set_status(self, status):
        self.order["status"] = status
        return self

    def build(self):
        return self.order