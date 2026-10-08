from patterns.behavioral.delivery_strategy import (
    NormalDelivery,
    ExpressDelivery,
    PremiumDelivery
)


def calculate_delivery_charge(
    delivery_type,
    distance
):

    if delivery_type == "normal":

        strategy = NormalDelivery()

    elif delivery_type == "express":

        strategy = ExpressDelivery()

    elif delivery_type == "premium":

        strategy = PremiumDelivery()

    else:

        raise ValueError(
            "Invalid delivery type. "
            "Use normal, express, or premium."
        )

    return strategy.calculate_charge(distance)