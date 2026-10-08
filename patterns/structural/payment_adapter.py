from abc import ABC, abstractmethod


class PaymentProcessor(ABC):

    @abstractmethod
    def process_payment(self, amount):
        pass


# Existing UPI payment provider
class UPIProvider:

    def make_upi_payment(self, amount):
        return {
            "provider": "UPI",
            "amount": amount,
            "status": "SUCCESS",
            "transaction_id": "UPI12345"
        }


# Existing Card payment provider
class CardProvider:

    def charge_card(self, amount):
        return {
            "provider": "CARD",
            "amount": amount,
            "status": "SUCCESS",
            "transaction_id": "CARD12345"
        }


# Adapter for UPI
class UPIAdapter(PaymentProcessor):

    def __init__(self):
        self.upi_provider = UPIProvider()

    def process_payment(self, amount):
        return self.upi_provider.make_upi_payment(amount)


# Adapter for Card
class CardAdapter(PaymentProcessor):

    def __init__(self):
        self.card_provider = CardProvider()

    def process_payment(self, amount):
        return self.card_provider.charge_card(amount)