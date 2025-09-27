from django.db import models

class Feedback(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def__str__(self):
        return f"feedback {self.id} - {self.comment[:30]}"

class MenuCategory(models.Model):
    name = models.CharField(max_length=100; unique=True)

    def__str__(self):
        return self.name
class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def__str__(self):
        return self.name
