from patterns.creational.food_prototype import Food


original_food = Food(
    "Chicken Biryani",
    180,
    "Main Course"
)


cloned_food = original_food.clone()


print("Original Food:")
print(original_food.display())


print("\nCloned Food:")
print(cloned_food.display())


print("\nAre they the same object?")
print(original_food is cloned_food)


cloned_food.name = "Chicken Biryani Special"
cloned_food.price = 220


print("\nAfter modifying cloned food:")

print("Original:")
print(original_food.display())

print("Clone:")
print(cloned_food.display())