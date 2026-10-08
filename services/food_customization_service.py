from patterns.structural.food_decorator import (
    BasicFood,
    ExtraEggDecorator,
    ExtraChickenDecorator,
    ExtraCheeseDecorator,
    ExtraRaitaDecorator,
    ExtraOnionDecorator,
    ExtraSalnaDecorator,
    ExtraParottaDecorator,
    ExtraFishDecorator,
    ExtraGravyDecorator,
    ExtraRiceDecorator
)


CUSTOMIZATION_RULES = {

    "chicken biryani": [
        {
            "id": "extra_egg",
            "name": "Extra Egg",
            "price": 20
        },
        {
            "id": "extra_chicken",
            "name": "Extra Chicken",
            "price": 50
        },
        {
            "id": "extra_raita",
            "name": "Extra Raita",
            "price": 15
        }
    ],

    "kari dosa": [
        {
            "id": "extra_egg",
            "name": "Extra Egg",
            "price": 20
        },
        {
            "id": "extra_chicken",
            "name": "Extra Chicken",
            "price": 50
        },
        {
            "id": "extra_onion",
            "name": "Extra Onion",
            "price": 10
        }
    ],

    "parotta": [
        {
            "id": "extra_parotta",
            "name": "Extra Parotta",
            "price": 20
        },
        {
            "id": "extra_salna",
            "name": "Extra Salna",
            "price": 15
        },
        {
            "id": "extra_egg",
            "name": "Egg",
            "price": 20
        }
    ],

    "fish curry": [
        {
            "id": "extra_fish",
            "name": "Extra Fish",
            "price": 70
        },
        {
            "id": "extra_gravy",
            "name": "Extra Gravy",
            "price": 20
        },
        {
            "id": "extra_rice",
            "name": "Extra Rice",
            "price": 30
        }
    ]
}


def get_customization_options(name, category=None):

    food_name = name.strip().lower()

    if food_name in CUSTOMIZATION_RULES:

        return CUSTOMIZATION_RULES[food_name]

    # Fallback based on category

    category_name = ""

    if category:
        category_name = category.strip().lower()


    if "biryani" in category_name:

        return CUSTOMIZATION_RULES[
            "chicken biryani"
        ]


    if "dosa" in category_name:

        return CUSTOMIZATION_RULES[
            "kari dosa"
        ]


    if "fish" in category_name:

        return CUSTOMIZATION_RULES[
            "fish curry"
        ]


    return [
        {
            "id": "extra_cheese",
            "name": "Extra Cheese",
            "price": 30
        }
    ]


def customize_food(
    name,
    price,
    extras,
    category=None
):

    food = BasicFood(
        name,
        price
    )


    available_options = get_customization_options(
        name,
        category
    )


    allowed_extras = {
        option["id"]: option
        for option in available_options
    }


    for extra in extras:

        if extra not in allowed_extras:

            raise ValueError(
                f"{extra} is not available "
                f"for {name}"
            )


        if extra == "extra_egg":

            food = ExtraEggDecorator(food)


        elif extra == "extra_chicken":

            food = ExtraChickenDecorator(food)


        elif extra == "extra_cheese":

            food = ExtraCheeseDecorator(food)


        elif extra == "extra_raita":

            food = ExtraRaitaDecorator(food)


        elif extra == "extra_onion":

            food = ExtraOnionDecorator(food)


        elif extra == "extra_salna":

            food = ExtraSalnaDecorator(food)


        elif extra == "extra_parotta":

            food = ExtraParottaDecorator(food)


        elif extra == "extra_fish":

            food = ExtraFishDecorator(food)


        elif extra == "extra_gravy":

            food = ExtraGravyDecorator(food)


        elif extra == "extra_rice":

            food = ExtraRiceDecorator(food)


    return {
        "food_name": food.get_name(),
        "base_price": price,
        "final_price": food.get_price(),
        "extras": extras,
        "available_options": available_options
    }