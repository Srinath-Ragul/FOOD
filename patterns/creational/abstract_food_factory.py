from abc import ABC, abstractmethod


# ---------- Abstract Products ----------

class MainCourse(ABC):

    @abstractmethod
    def prepare(self):
        pass


class Beverage(ABC):

    @abstractmethod
    def prepare(self):
        pass


# ---------- Madurai Products ----------

class MaduraiMainCourse(MainCourse):

    def prepare(self):
        return "Preparing Madurai main course"


class MaduraiBeverage(Beverage):

    def prepare(self):
        return "Preparing Madurai beverage"


# ---------- Premium Products ----------

class PremiumMainCourse(MainCourse):

    def prepare(self):
        return "Preparing premium main course"


class PremiumBeverage(Beverage):

    def prepare(self):
        return "Preparing premium beverage"


# ---------- Abstract Factory ----------

class FoodFactory(ABC):

    @abstractmethod
    def create_main_course(self):
        pass

    @abstractmethod
    def create_beverage(self):
        pass


# ---------- Concrete Factories ----------

class MaduraiFoodFactory(FoodFactory):

    def create_main_course(self):
        return MaduraiMainCourse()

    def create_beverage(self):
        return MaduraiBeverage()


class PremiumFoodFactory(FoodFactory):

    def create_main_course(self):
        return PremiumMainCourse()

    def create_beverage(self):
        return PremiumBeverage()