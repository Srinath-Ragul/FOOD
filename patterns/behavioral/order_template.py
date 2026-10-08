from abc import ABC, abstractmethod


class OrderProcessor(ABC):

    def process_order(self):

        self.validate_order()

        self.calculate_amount()

        self.process_payment()

        self.confirm_order()

    @abstractmethod
    def validate_order(self):
        pass

    @abstractmethod
    def calculate_amount(self):
        pass

    @abstractmethod
    def process_payment(self):
        pass

    def confirm_order(self):
        print("Order confirmed successfully.")


class NormalOrderProcessor(OrderProcessor):

    def validate_order(self):
        print("Validating normal order...")

    def calculate_amount(self):
        print("Calculating normal order amount...")

    def process_payment(self):
        print("Processing normal order payment...")


class PreOrderProcessor(OrderProcessor):

    def validate_order(self):
        print("Validating pre-order...")

    def calculate_amount(self):
        print("Calculating pre-order amount...")

    def process_payment(self):
        print("Processing pre-order payment...")