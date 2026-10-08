from flask import Blueprint, request, jsonify

from services.customer_service import (
    get_all_customers,
    add_customer
)


customer_controller = Blueprint(
    "customer_controller",
    __name__
)


@customer_controller.route("/customers", methods=["GET"])
def customers():

    result = get_all_customers()

    return jsonify(result)


@customer_controller.route("/customers", methods=["POST"])
def create_customer():

    data = request.get_json()

    name = data["name"]
    email = data["email"]
    password = data["password"]

    customer_id = add_customer(
        name,
        email,
        password
    )

    return jsonify({
        "message": "Customer created successfully",
        "customer_id": customer_id
    }), 201