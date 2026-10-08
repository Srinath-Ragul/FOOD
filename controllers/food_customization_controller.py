from flask import Blueprint, request, jsonify

from services.food_customization_service import (
    customize_food,
    get_customization_options
)


food_customization_controller = Blueprint(
    "food_customization_controller",
    __name__
)


@food_customization_controller.route(
    "/food/customize/options",
    methods=["GET"]
)
def customization_options():

    name = request.args.get(
        "name",
        ""
    )

    category = request.args.get(
        "category",
        ""
    )


    options = get_customization_options(
        name,
        category
    )


    return jsonify({
        "food_name": name,
        "options": options
    })


@food_customization_controller.route(
    "/food/customize",
    methods=["POST"]
)
def customize():

    data = request.get_json()


    try:

        result = customize_food(

            name=data["name"],

            price=data["price"],

            extras=data.get(
                "extras",
                []
            ),

            category=data.get(
                "category"
            )

        )


        return jsonify(result), 200


    except ValueError as error:

        return jsonify({
            "error": str(error)
        }), 400