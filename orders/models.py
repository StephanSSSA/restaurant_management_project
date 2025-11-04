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

    class Coupon(models.Model):
        code = models.CharField(max_length=50, unique=True)
        discount_percentage = models.DecimalField(max_digit=5, decimal_places=2)
        is_active = models.BooleanField(default=True)
        valid_from = models.DateField()
        valid_until = models.DateField()

        def__str__(self):
            return self.code

    class Restaurant(models.Model):
        name = models.CharField(max_length=255)
        address = models.TextField()
        phone_number = models.CharField(max_length=20)
        email = models.EmailField(blank=True, null=True)
        has_delivery = models.BooleanField(default=False)

        def__str__(self):
            return self.name

