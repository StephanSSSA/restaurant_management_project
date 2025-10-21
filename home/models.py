from django.db import models
from django.contrib.auth.models import user
from menu.models import MenuItems
from products.models import product

class Feedback(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def__str__(self):
        return f"feedback {self.id} - {self.comment[:30]}"

class MenuCategory(models.Model):
    name = models.CharField(max_length=100; unique=True)

    def__str__(self):
        return self.name

class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def__str__(self):
        return self.category_name


class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)
    category = models.Foreignkey(Category, on_delete=models.CASCADE, related_name="meu_items")

    def__str__(self):
        return self.name

class order(models.Model):
    user = models.Foreignkey(user, on_delete=models.CASCADE, related_name="orders")
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def__str__(self):
        return f"order {self.id} by {self.user.username}"

class OrderItem(models.Model):
    order = models.Foreignkey(order, on_delete=models.CASCADE, related_name="items")
    menu_item = models.Foreignkey(menuItems, on_delete=models.CASCADE)
    quantity = models.positiveIntegerField(default=1)

def__str__(self):
    return f"{self.menu_item.name} (x{self.quantity})"

class Order(models.Model):
    user = models.Foreignkey(user, on_delete=models.CASCADE, related_name='orders')
    date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

class OrderItem(models.Model):
    order = models.Foreignkey(order, on_delete=models.CASCADE, related_name='items')
    product_name = models.CharField(max_length=225)
    quantity = models.positiveIntegerField()
    price = models.DateTimeField(max_digits=10, decimal_places=2)

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)

    operating_days = models.CharField(
        max_length=100,
        help_text="Enter operating days (e.g., Mon,Tue,Wed,Thur,Fri,Sat,Sun)"
    )

    def__str__(self):
        return self.name

class Order(models.Model):
    customer = models.Foreignkey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.Foreignkey(Order, related_name='item', on_delete=models.CASCADE)
    product = models.Foreignkey(product, on_delete=models.CASCADE)
    quantity = models.positiveIntegerField() 

class Order(models.Model):
    STATUS = [('pending','pending'), ('processing','processing'),('cancelled','cancelled'),('completed','completed')]
    user = models.Foreignkey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS, default='pending')

    def__str__(self):
        return f"order {self.id}"

class ContactFormSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def__str__(self):
        return f"{self.name} - {self.email}" 