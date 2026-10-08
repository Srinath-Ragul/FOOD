from flask import Blueprint, request, jsonify

from services.order_service import create_order


order_controller = Blueprint(
    "order_controller",
    __name__
)


@order_controller.route(
    "/orders",
    methods=["POST"]
)
def place_order():

    data = request.get_json()

    result = create_order(
        customer_id=data["customer_id"],
        restaurant_id=data["restaurant_id"],
        order_type=data["order_type"],
        items=data["items"],
        delivery_type=data["delivery_type"],
        distance=data["distance"]
    )

    return jsonify(result), 201