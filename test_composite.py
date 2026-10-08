from patterns.structural.food_composite import (
    FoodItem,
    FoodGroup
)


biryani = FoodItem(
    "Chicken Biryani",
    180
)

parotta = FoodItem(
    "Parotta",
    40
)

fish_curry = FoodItem(
    "Fish Curry",
    150
)


main_course = FoodGroup(
    "Madurai Main Course"
)

main_course.add(biryani)
main_course.add(parotta)
main_course.add(fish_curry)


print("Group:", main_course.get_name())

print("Items:")

for item in main_course.items:
    print(
        item.get_name(),
        "₹",
        item.get_price()
    )


print("Total:", main_course.get_price())