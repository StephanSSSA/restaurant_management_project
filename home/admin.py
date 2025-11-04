from django.contrib import admin
from .models import Restaurant
from .models import MenuItem, NutritionalInformation

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'operating_days')

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_featured')

@admin.register(NutritionalInformation)
class NutritionalInformationAdmin(admin.ModelAdmin):
    list_display = ('menu_item', 'calories', 'protein_grams', 'fat_grams', 'carbohydrate_grams')

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'has_delivery')
