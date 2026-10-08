from abc import ABC, abstractmethod


class FoodItem(ABC):

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_price(self):
        pass


class BasicFood(FoodItem):

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price


class FoodDecorator(FoodItem):

    def __init__(self, food):
        self.food = food

    def get_name(self):
        return self.food.get_name()

    def get_price(self):
        return self.food.get_price()


class ExtraEggDecorator(FoodDecorator):

    def get_name(self):
        return self.food.get_name() + " + Extra Egg"

    def get_price(self):
        return self.food.get_price() + 20


class ExtraChickenDecorator(FoodDecorator):

    def get_name(self):
        return self.food.get_name() + " + Extra Chicken"

    def get_price(self):
        return self.food.get_price() + 50


class ExtraCheeseDecorator(FoodDecorator):

    def get_name(self):
        return self.food.get_name() + " + Extra Cheese"

    def get_price(self):
        return self.food.get_price() + 30


class ExtraRaitaDecorator(FoodDecorator):

    def get_name(self):
        return self.food.get_name() + " + Extra Raita"

    def get_price(self):
        return self.food.get_price() + 15


class ExtraOnionDecorator(FoodDecorator):

    def get_name(self):
        return self.food.get_name() + " + Extra Onion"

    def get_price(self):
        return self.food.get_price() + 10


class ExtraSalnaDecorator(FoodDecorator):

    def get_name(self):
        return self.food.get_name() + " + Extra Salna"

    def get_price(self):
        return self.food.get_price() + 15


class ExtraParottaDecorator(FoodDecorator):

    def get_name(self):
        return self.food.get_name() + " + Extra Parotta"

    def get_price(self):
        return self.food.get_price() + 20


class ExtraFishDecorator(FoodDecorator):

    def get_name(self):
        return self.food.get_name() + " + Extra Fish"

    def get_price(self):
        return self.food.get_price() + 70


class ExtraGravyDecorator(FoodDecorator):

    def get_name(self):
        return self.food.get_name() + " + Extra Gravy"

    def get_price(self):
        return self.food.get_price() + 20


class ExtraRiceDecorator(FoodDecorator):

    def get_name(self):
        return self.food.get_name() + " + Extra Rice"

    def get_price(self):
        return self.food.get_price() + 30