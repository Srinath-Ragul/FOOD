from flask import Blueprint, request, jsonify

from services.food_service import (
    get_food_by_restaurant,
    add_food
)


food_controller = Blueprint(
    "food_controller",
    __name__
)


@food_controller.route("/restaurants/<int:restaurant_id>/foods",
                       methods=["GET"])
def get_foods(restaurant_id):

    foods = get_food_by_restaurant(restaurant_id)

    return jsonify(foods)


@food_controller.route("/restaurants/<int:restaurant_id>/foods",
                       methods=["POST"])
def create_food(restaurant_id):

    data = request.get_json()

    food_id = add_food(
        restaurant_id,
        data["name"],
        data["price"],
        data["category"]
    )

    return jsonify({
        "message": "Food added successfully",
        "food_id": food_id
    }), 201