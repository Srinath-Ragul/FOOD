class OrderMemento:

    def __init__(self, status):
        self.status = status


class Order:

    def __init__(self, order_id, status):
        self.order_id = order_id
        self.status = status

    def save(self):
        return OrderMemento(self.status)

    def restore(self, memento):
        self.status = memento.status

    def change_status(self, new_status):
        self.status = new_status


class OrderHistory:

    def __init__(self):
        self.history = []

    def save(self, memento):
        self.history.append(memento)

    def get_last(self):

        if not self.history:
            return None

        return self.history.pop()