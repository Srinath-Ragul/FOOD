from patterns.structural.food_flyweight import (
    FoodCategoryFactory
)


biryani_category = FoodCategoryFactory.get_category(
    "Main Course"
)

parotta_category = FoodCategoryFactory.get_category(
    "Main Course"
)

juice_category = FoodCategoryFactory.get_category(
    "Beverage"
)


print(
    biryani_category.display(
        "Chicken Biryani",
        180
    )
)

print(
    parotta_category.display(
        "Parotta",
        40
    )
)

print(
    juice_category.display(
        "Lemon Juice",
        50
    )
)


print(
    "\nNumber of shared category objects:",
    FoodCategoryFactory.get_category_count()
)


print(
    "Main Course objects are same:",
    biryani_category is parotta_category
)