from patterns.behavioral.order_memento import (
    Order,
    OrderHistory
)


order = Order(
    order_id=1,
    status="PLACED"
)

history = OrderHistory()


print("Initial status:")
print(order.status)


# Save PLACED state
history.save(order.save())


# Change to ACCEPTED
order.change_status("ACCEPTED")

print("\nAfter status change:")
print(order.status)


# Save ACCEPTED state
history.save(order.save())


# Change to PREPARING
order.change_status("PREPARING")

print("\nAfter another status change:")
print(order.status)


# Restore previous state
memento = history.get_last()

order.restore(memento)

print("\nAfter restore:")
print(order.status)