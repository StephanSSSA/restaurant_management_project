import datetime import datetime
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.db import DatabaseError
from .Models import MenuItem
from rest_framework.generics import ListAPIView
from .models import MenuCategory
from .serializers import MenuCategorySerializer
from rest_framework import viewsets, pagination
from rest_framework.response import Response
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework.response import Response
from rest_framework import status, generics
from .models import MenuItems
from .serializers import MenuItemSerializer
from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemIngredientsSerializer

def index(request):
    restarunt_name = settings.RESTARUNT_NAME
    return render(request, 'home/index.html',{"restarunt_name": restuarant_name})
def about(request):
    return render(request, "about.html")
def contact(request):
    return render(request, "home/contact.html")
def home(request):
    phone_number = settings.RESTARUNT_PHONE
    return render(request, "home.html", {"phone_number": phone_number})
def home(request):
    return render(request, "home.html", {
        "restuarant_name": "Spicy Food Corner",
        "phone number": "+91 7695960636",
        "current_year": datetime.now().year,
        "opening_hours": "Mon-Fri: 11am-9pm, Sat-Sun: 10am-10pm",
    })

def reservations(request):
    return render(request, "home/reservations.html",{
        "current_year": datetime.date.today().year,
        })

def menu_view(request):
    try:
        items = MenuItem.objects.all()
        return render(request, "menu.html", {"items": iems})
    except Exception as e:
        return HttpResponse(f"An unexcepted error occured: {str(e)}", status=500)
class MenuCategoryListView(ListAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer

class MenuItemPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50

class MenuItemViewSet(viewset.ViewSet):

    def list(self, request):
        query = request.query_params.get('search', None)
        queryset = MenuItem.objects.all()

        if query:
            queryset = queryset.filter(name__icontains=query)

        paginator = MenuItemPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = MenuItemSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

class MenuItemViewset(viewset.ModelViewset):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAdminUser]

class MenuItemsByCategoryview(generics.ListAPIView):
    serializer_class = MenuItemSerializer

    def get_queryset(self):
        queryset = MenuItems.objects.all()
        category = self.request.query_params.get("category", None)

        if category:
            queryset = queryset.filter(category__category_name__iexact=category)
            return queryset

class  MenuItemIngredientsView(generics.RetrieveAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemIngredientsSerializer