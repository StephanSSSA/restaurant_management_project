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
from rest_framework.views import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import is Authenticated
from .models import Order
from .serializers import OrderSerializer
from rest_framework import generics
from .models import Table
from .serializers import TableSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from .models import ContactFormSubmission
from .serializers import ContactFormSubmissionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import send_custom_email
from .models import ContactFormSubmission
from .serializers import ContactFormSubmissionSerializer

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

class OrderHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        user = request.user
        orders = Order.objects.filter(user=user).order_by("-created_at")
        serializer = OrderSerializer(orders, many=True) return Response(serializer.data)

    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        return Response(OrderSerializer(orders, many=True).data)
    
    class TableDetailAPIView(generics.RetrieveAPIView):
        queryset = Table.objects.all()
        serializer_class = TableSerializer
        lookup_field = 'pk'

    class AvailableTableAPIView(generics.ListAPIView):
        queryset = Table.objects.filter(is_available=True)
        serializer_class = TableSerializer
    
    class OrderCreateAPIView(APIView):
        def post(self, request):
            customer_email = request.data.get('email')
            customer_name = request.data.get('name')
            total_amount = request.data.get('total')
            order = Order.objects.create(
                customer_name=customer_name,
                customer_email=customer_email,
                total_amount=total_amount
            )

            email_status = send_order_confirmation_email(
                order_id=order.id,
                customer_email=customer_email,
                customer_name=customer_name,
                total_amount=total_amount
            )

            return Response({
                "order_id": order.id,
                "email_status": email_status
            })
    
    class ContactFormSubmissionView(generics.CreateAPIView):
        queryset = ContactFormSubmission.objects.all()
        serializer_class = ContactFormSubmissionSerializer

        def create(self, request, args, kwargs):
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"messge"; "your message has been received!", "data": serializer.data},
                    status=status.HTTP_201_CREATED
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    class ContactFormSubmissionView(APIView):
        def post(self, request):
            serializer = ContactFormSubmissionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()

                recipient = serializer.validated_data['email']
                subject = "Thank you for contacting us!"
                message = f"Hello {serializer.validated_data['name']},\n\nwe received message:\n\{serializer.validatd_data['message']}\n\nwe'Il get back to you soon."

                email_sent = send_custom_email(recipient, subject, message)

                if email_sent:
                    return Response({"message": "contact form submitted and email sent successfully."}, status=status.HTTP_201_CREATED)
                else:
                    return Response({"message": "Form saved, but email could not be sent."}, status=status.HTTP_500_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    class FeaturedMenuItemView(generics.ListAPIView):

        serializer_class = MenuItemSerializer

        def get_queryset(self):
            return MenuItem.object.filter(is_featured=True)