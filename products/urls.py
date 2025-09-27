from django.urls import path
from .views import *

urlpatterns = [
    path('items/', ItemView.as_view(), name='item-list'),
    path("menu/", views.menu, name="menu")
    path('register/' RegisterUserView.as_view(), name='register-user'),
]