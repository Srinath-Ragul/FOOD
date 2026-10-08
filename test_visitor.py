from patterns.behavioral.order_visitor import (
    FoodItem,
    DeliveryItem,
    OrderReportVisitor,
    OrderTotalVisitor
)


biryani = FoodItem(
    "Chicken Biryani",
    180,
    2
)

parotta = FoodItem(
    "Parotta",
    40,
    3
)

delivery = DeliveryItem(5)


report_visitor = OrderReportVisitor()

print("ORDER REPORT")
print("----------------")

print(
    biryani.accept(report_visitor)
)

print(
    parotta.accept(report_visitor)
)

print(
    delivery.accept(report_visitor)
)


total_visitor = OrderTotalVisitor()

biryani.accept(total_visitor)
parotta.accept(total_visitor)
delivery.accept(total_visitor)


print("\nTOTAL AMOUNT")
print("----------------")

print(
    "Total: ₹",
    total_visitor.get_total()
)