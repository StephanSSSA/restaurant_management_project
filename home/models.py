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
