from django.db import models

class OrderStatus(models.Model):
    name = models.CharField(max_length=50; unique=True)

    def__str__(self):
        return self.name

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    order_date = models.DateTimeField(auto_now_add=True)

    status = models.Foreignkey(
        OrderStatus,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def__str__(self):
        return f"Order {self.id} - {self.customer_name}"

    class ActiveOrderManager(models.Manager):
        def get_active_orders(self):
            return self.get_queryset().filter(status__in=['pending', 'processing'])
