from django.db import models
from django.db.models import Count

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

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    is_vegan = models.BooleanField(default=False)

    def__str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    ingredients = models.ManyToManyField(Ingredient, related_name='menu_items')

    def__str__(self):
        return self.name

class MenuItemManager(models.Manager):
    def get_top_selling_items(self, num_items=5):

        return (
            self.annotate(total_orders=Count('order_items'))
            .order_by('-total_orders')[:num_items]
        )