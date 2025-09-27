from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewset

router = DefaultRouter()
router.register(r'menu-items', MenuItemViewset, basename='menuitem')

urlpatterns = [
    path("menu/", views.menu, name="menu"),
    path('', include(router.urls)),
]