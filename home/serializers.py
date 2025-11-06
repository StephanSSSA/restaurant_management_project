from rest_framework import serializers
from .models import MenuItems
from .models import MenuItem, Ingredient


class MenuCategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.category_name", read_only=True)
    class Meta:
        model = MenuCategory
        fields = ['id', 'name', 'description', 'price', 'category_name']

    def validate_price(self, value):
        if value <=0:
            raise serializers.ValidationError("price must be a positive number.")
        return value

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'is_vegan']

class MenuItemIngredientsSerializer(serializers.Modelserializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'ingredients']