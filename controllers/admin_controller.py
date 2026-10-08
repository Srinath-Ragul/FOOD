from flask import (
    Blueprint,
    jsonify,
    render_template
)

from services.admin_service import (
    get_all_orders
)

from services.order_state_service import (
    move_order_to_next_state
)


admin_controller = Blueprint(
    "admin_controller",
    __name__
)


@admin_controller.route(
    "/restaurant-dashboard",
    methods=["GET"]
)
def restaurant_dashboard():

    return render_template(
        "restaurant_dashboard.html"
    )


@admin_controller.route(
    "/admin/orders",
    methods=["GET"]
)
def admin_orders():

    orders = get_all_orders()

    return jsonify(
        orders
    )


@admin_controller.route(
    "/admin/orders/<int:order_id>/next",
    methods=["PUT"]
)
def admin_next_order_state(
    order_id
):

    result = move_order_to_next_state(
        order_id
    )


    if "error" in result:

        return jsonify(
            result
        ), 400


    return jsonify(
        result
    )