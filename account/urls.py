from django.urls import path
from .views import UserprofileViewset

user_profile = UserprofileViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
})

urlpatterns = [
    path('profile/', user_profile, name='user-profile'),
]