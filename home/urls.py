from django.contrib impot admin
from django.urls import path,include
from .views import *
from django.urls import path
from .views import MenuCategoryListView
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewSet
from .views import MenuItemsByCategoryView
from .views import TableDetailAPIView
from django.urls import path
from .views import AvailableTableAPIView

router = DefaultRouter()
router.register(r'menu-items', MenuItemViewSet, basename='menuitem')

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',include('home.urls')),
    path("about/", views.about, name="about"),
    path("products/", include(products.urls)),
    path("contact/", views.contact, name="contact"),
    path("", view.home, name="home"),
    path("reservations/", view.reservations name="reservations"),
    path("menu/", views.menu_view, name="menu"),
    path("categories/", MenuCategoryListView.as_view(), name="menu-categories"),
    path('', include(router.urls))
    path('api/users/', include('users.urls')),
    path("menu-items/", MenuItemsByCategoryView.as_view(), name="menu-items-by-category")
    path("order-history/", Order-HistoryView.as_view(), name="order-history"),
    path('api/tables/<int:pk>/', TableDetailAPIView.as_view(), name='table-detail'),
    path('api/tables/available', AvailableTableAPIView.as_view(), name='available_tables_api')
    path('api/', include('accounts.urls')),
]