from django.urls import path
from .views import *

urlpatterns = [
    path("menu/", views.menu, name="menu"),
]