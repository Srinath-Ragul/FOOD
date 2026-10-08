from flask import Blueprint, request, jsonify

from patterns.structural.order_proxy import OrderProxy


order_proxy_controller = Blueprint(
    "order_proxy_controller",
    __name__
)


@order_proxy_controller.route(
    "/orders/<int:order_id>/secure",
    methods=["GET"]
)
def get_secure_order(order_id):

    customer_id = request.args.get(
        "customer_id",
        type=int
    )

    if customer_id is None:
        return jsonify({
            "error": "customer_id is required"
        }), 400

    proxy = OrderProxy()

    result = proxy.get_order(
        order_id,
        customer_id
    )

    if "error" in result:

        if result["error"] == "Order not found":
            return jsonify(result), 404

        return jsonify(result), 403

    return jsonify(result)