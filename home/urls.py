fromdjango.contrib impot adminfrom django.urls import path,include
from .views import *

urlpatterns = [
    path('',views.index, name='index'),
]