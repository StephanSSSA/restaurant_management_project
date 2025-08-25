from django.contrib impot admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',include('home.urls')),
    path("about/", views.about, name="about"),
    path("products/", include(products.urls)),
]