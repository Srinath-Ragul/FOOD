from flask import Blueprint, request, jsonify

from patterns.structural.order_facade import OrderFacade


order_facade_controller = Blueprint(
    "order_facade_controller",
    __name__
)


@order_facade_controller.route(
    "/orders/place",
    methods=["POST"]
)
def place_order():

    data = request.get_json()

    try:

        facade = OrderFacade()

        result = facade.place_order(
            customer_id=data["customer_id"],
            restaurant_id=data["restaurant_id"],
            order_type=data["order_type"],
            items=data["items"],
            delivery_type=data["delivery_type"],
            distance=data["distance"],
            payment_method=data["payment_method"]
        )

        return jsonify(result), 201

    except ValueError as error:

        return jsonify({
            "error": str(error)
        }), 400