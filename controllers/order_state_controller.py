from flask import Blueprint, jsonify

from services.order_state_service import (
    get_order_status,
    move_order_to_next_state
)


order_state_controller = Blueprint(
    "order_state_controller",
    __name__
)


@order_state_controller.route(
    "/orders/<int:order_id>/status",
    methods=["GET"]
)
def order_status(order_id):

    status = get_order_status(order_id)

    if status is None:

        return jsonify({
            "error": "Order not found"
        }), 404

    return jsonify({
        "order_id": order_id,
        "status": status
    })


@order_state_controller.route(
    "/orders/<int:order_id>/next",
    methods=["PUT"]
)
def next_order_state(order_id):

    result = move_order_to_next_state(order_id)

    if "error" in result:

        return jsonify(result), 404

    return jsonify(result)