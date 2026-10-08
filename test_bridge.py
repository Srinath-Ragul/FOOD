from patterns.structural.delivery_bridge import (
    SMSNotification,
    EmailNotification,
    NormalDeliveryService,
    ExpressDeliveryService
)


sms = SMSNotification()
email = EmailNotification()


normal_delivery = NormalDeliveryService(sms)
express_delivery = ExpressDeliveryService(email)


print(normal_delivery.update_delivery(1))

print(express_delivery.update_delivery(1))