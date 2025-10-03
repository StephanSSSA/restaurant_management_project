from rest_framework import serializers
from .models import MenuItems


class MenuCategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.category_name", read_only=True)
    class Meta:
        model = MenuCategory
        fields = ['id', 'name', 'description', 'price', 'category_name']

    def validate_price(self, value):
        if value <=0:
            raise serializers.ValidationError("price must be a positive number.")
        return value