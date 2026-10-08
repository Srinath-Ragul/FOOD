from flask import Blueprint, request, jsonify

from services.payment_service import process_payment


payment_controller = Blueprint(
    "payment_controller",
    __name__
)


@payment_controller.route(
    "/payments",
    methods=["POST"]
)
def make_payment():

    data = request.get_json()

    try:

        result = process_payment(
            order_id=data["order_id"],
            payment_method=data["payment_method"],
            amount=data["amount"]
        )

        return jsonify(result), 201

    except ValueError as error:

        return jsonify({
            "error": str(error)
        }), 400