from abc import ABC, abstractmethod


class FoodComponent(ABC):

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_price(self):
        pass


class FoodItem(FoodComponent):

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price


class FoodGroup(FoodComponent):

    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, food):
        self.items.append(food)

    def remove(self, food):
        if food in self.items:
            self.items.remove(food)

    def get_name(self):
        return self.name

    def get_price(self):

        total = 0

        for item in self.items:
            total += item.get_price()

        return total