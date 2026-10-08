from flask import Blueprint, request, jsonify

from services.restaurant_service import (
    get_all_restaurants,
    add_restaurant
)


restaurant_controller = Blueprint(
    "restaurant_controller",
    __name__
)


@restaurant_controller.route("/restaurants", methods=["GET"])
def restaurants():

    result = get_all_restaurants()

    return jsonify(result)


@restaurant_controller.route("/restaurants", methods=["POST"])
def create_restaurant():

    data = request.get_json()

    name = data["name"]
    location = data["location"]
    rating = data["rating"]

    restaurant_id = add_restaurant(
        name,
        location,
        rating
    )

    return jsonify({
        "message": "Restaurant created successfully",
        "restaurant_id": restaurant_id
    }), 201