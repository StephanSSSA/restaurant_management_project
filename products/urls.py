from django.urls import path
from .views import *
from .views import CouponValidationView

urlpatterns = [
    path('items/', ItemView.as_view(), name='item-list'),
    path("menu/", views.menu, name="menu")
    path('register/' RegisterUserView.as_view(), name='register-user'),
    path('coupons/validate/', CouponValidationView.as_view(), name='coupon-validate'),
]