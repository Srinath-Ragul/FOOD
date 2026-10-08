class FoodCategory:

    def __init__(self, category_name):
        self.category_name = category_name

    def display(self, food_name, price):
        return (
            f"{food_name} | "
            f"Category: {self.category_name} | "
            f"Price: ₹{price}"
        )


class FoodCategoryFactory:

    _categories = {}

    @classmethod
    def get_category(cls, category_name):

        if category_name not in cls._categories:

            cls._categories[category_name] = FoodCategory(
                category_name
            )

        return cls._categories[category_name]

    @classmethod
    def get_category_count(cls):
        return len(cls._categories)