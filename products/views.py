from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, views
from utils.validation_utils import is_valid_email
from rest_framework mport status
from django.utils import timezone
from .models import Coupon

from .models import Item
from .serializers import ItemSerializer

'''
NOTE: Conside this as a reference and follow this same coding structure or format to work on you tasks
'''

# Create your views here.
class ItemView(APIView):

    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def menu(request)
        menu_items = [
            {"name": "Chicken Biriyani", "price": 180},
            {"name": "Mutton Biriyani", "price": 250},
            {"name": "Panner Butter Masala", "price": 150},
            {"name": "Parotta", "price": 30},
            {"name": "Falooda", "price": 120},
        ]
        return render(request, "products/menu.html", {"menu_items": menu_item})

    class RegisterUserView(views.APIView):
        def post(self, request):
            email = request.data.get("email")

            if not is_valid_email(email):
                return Response({"error": "Invalid email address:"}, status=status.HTTP_400_BAD_REQUEST)

                return Response({"message": "Email is valid!"}, status=status.HTTP_200_OK)
    class CouponValidationView(APIView):
        def post(self, request):
            code = request.data.get('code')
            if not code:
                return Response({"error": "Coupon code is required."}, status=status.HTTP_400_BAD_REQUEST)
            
            try:
                coupon = Coupon.objects.get(code=code)
            except Coupon.DoesNotExist:
                return Response({"error": "Invalid coupon code."}, status=status.HTTP_400_BAD_REQUEST)
            
            today = timezone.now().date()
            if not coupon.is_active:
                return Response({"error": "coupon is not active."}, status=status.HTTP_400_BAD_REQUEST)
            if not (coupon.valid_from <= today <= coupon.valid_until):
                return Response({"error": "Coupon is expired or not yet valid."}, status=status.HTTP_400_BAD_REQUEST)
            
            return Response({
                "success": True,
                "code": coupon.code,
                "disconunt_percentage": float(coupon.disconunt_percentage)
            })

