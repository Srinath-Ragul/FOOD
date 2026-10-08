class OrderItemCollection:

    def __init__(self, items):
        self.items = items

    def create_iterator(self):
        return OrderItemIterator(self.items)


class OrderItemIterator:

    def __init__(self, items):
        self.items = items
        self.index = 0

    def has_next(self):
        return self.index < len(self.items)

    def next(self):

        if not self.has_next():
            return None

        item = self.items[self.index]

        self.index += 1

        return item