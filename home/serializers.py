from rest_framework import serializers
from .models import MenuItem
from .models import MenuCategory

class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ['id', 'name', 'description', 'price', 'availabe']

    def validate_price(self, value):
        if value <=0:
            raise serializers.ValidationError("price must be a positive number.")
        return value