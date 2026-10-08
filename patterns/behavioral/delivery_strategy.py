from abc import ABC, abstractmethod


class DeliveryStrategy(ABC):

    @abstractmethod
    def calculate_charge(self, distance):
        pass


class NormalDelivery(DeliveryStrategy):

    def calculate_charge(self, distance):

        if distance <= 3:
            return 30

        elif distance <= 7:
            return 50

        else:
            return 70


class ExpressDelivery(DeliveryStrategy):

    def calculate_charge(self, distance):

        if distance <= 3:
            return 60

        elif distance <= 7:
            return 90

        else:
            return 120


class PremiumDelivery(DeliveryStrategy):

    def calculate_charge(self, distance):

        if distance <= 3:
            return 100

        elif distance <= 7:
            return 140

        else:
            return 180