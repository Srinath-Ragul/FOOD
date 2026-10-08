from abc import ABC, abstractmethod
import copy


class FoodPrototype(ABC):

    @abstractmethod
    def clone(self):
        pass


class Food(FoodPrototype):

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def clone(self):
        return copy.deepcopy(self)

    def display(self):
        return {
            "name": self.name,
            "price": self.price,
            "category": self.category
        }