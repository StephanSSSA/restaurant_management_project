from rest_framework import serializers
from .models import MenuItems
from .models import Order, OrderItem
from .models import Table
from django.contrib.auth.models import user
from .models import Order


class MenuCategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.category_name", read_only=True)
    class Meta:
        model = MenuCategory
        fields = ['id', 'name', 'description', 'price', 'category_name']

    def validate_price(self, value):
        if value <=0:
            raise serializers.ValidationError("price must be a positive number.")
        return value

class OrderItemSerializer(serializers.ModelSerializer):
    menu_item.name = serializers.CharField(source="menu_item.name", read_only=True)
    price = serializers.DecimalField(source="menu_item.price", max_digits=8, decimal_places=2, read_only=True)
    class Meta:
        model = OrderItem
        fields = ["menu_item_name", "quantity", "price"]

    class OrderSerializer(serializers.ModelSerializer):
        items = OrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ["id", "created_at", "total_price", "items"]
    
    class TableSerializer(serializers.ModelSerializer):
        class Meta:
            model = Table
            fields = ['table_number', 'capacity', 'is_available']
    
    class Userprofileserializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ['first_name', 'last_name', 'email']
            read_only_fields = ['username']
    
    class OrderItemSerializer(serializers.ModelSerializer):
        class Meta:
            model = OrderItem
            fields = ['product', 'quantity']
    class OrderItemSerializer(serializers.ModelSerializer):
        items = OrderItemSerializer(many=True, read_only=True)
        class Meta:
            model = Order
            fields = ['id', 'customer', 'total_price', 'created_at', 'items']
    
    class OrderSerializer(serializers.ModelSerializer):
        class Meta:
            model = Order
            fields = '__all__'