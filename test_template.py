from patterns.behavioral.order_template import (
    NormalOrderProcessor,
    PreOrderProcessor
)


print("NORMAL ORDER")
print("----------------")

normal_order = NormalOrderProcessor()

normal_order.process_order()


print("\nPRE-ORDER")
print("----------------")

pre_order = PreOrderProcessor()

pre_order.process_order()