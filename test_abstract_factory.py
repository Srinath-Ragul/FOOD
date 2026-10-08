from patterns.creational.abstract_food_factory import (
    MaduraiFoodFactory,
    PremiumFoodFactory
)


print("MADURAI FOOD FACTORY")
print("--------------------")

madurai_factory = MaduraiFoodFactory()

main_course = madurai_factory.create_main_course()
beverage = madurai_factory.create_beverage()

print(main_course.prepare())
print(beverage.prepare())


print("\nPREMIUM FOOD FACTORY")
print("--------------------")

premium_factory = PremiumFoodFactory()

main_course = premium_factory.create_main_course()
beverage = premium_factory.create_beverage()

print(main_course.prepare())
print(beverage.prepare())