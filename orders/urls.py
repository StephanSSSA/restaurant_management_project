from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewset
from .views import OrderDetailView

router = DefaultRouter()
router.register(r'menu-items', MenuItemViewset, basename='menuitem')

urlpatterns = [
    path("menu/", views.menu, name="menu"),
    path('', include(router.urls)),
    path('<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
]