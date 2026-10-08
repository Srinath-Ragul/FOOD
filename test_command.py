from patterns.behavioral.order_command import (
    AcceptOrderCommand,
    PrepareOrderCommand,
    CancelOrderCommand,
    OrderInvoker
)


invoker = OrderInvoker()


accept_command = AcceptOrderCommand(1)

invoker.set_command(accept_command)

print("Accept Command:")
print(invoker.execute_command())


prepare_command = PrepareOrderCommand(1)

invoker.set_command(prepare_command)

print("\nPrepare Command:")
print(invoker.execute_command())


cancel_command = CancelOrderCommand(1)

invoker.set_command(cancel_command)

print("\nCancel Command:")
print(invoker.execute_command())