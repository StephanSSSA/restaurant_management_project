import string
import secrets
from .models import Coupon 
from datetime import date, time
from django.db.models import Sum
from .models import Order
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
import logging
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet
from .models import Order
from django.db import models
from django.contrib.auth.models import user
from .utils import generate_unique_order_id
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from datetime import datetime
from home.models import DailyOperatingHours


def generate_coupon_code(length=10):
    characters = string.ascii_uppercase + string.digits

    while True:
        code = ''.join(secrets.choice(characters) for _ in range(length))

        if not Coupon.objects.filter(code=code).exist():
            return code

def get_daily_sales_total(target_date: date):

    orders = Order.objects.filter(created_at__date=target_date)
    total = orders.aggregate(total_sum=Sum('toal_price'))['total_sum']

    return total or 0

def is_restaurant_open():
    now = datetime.now()
    current_day = now.weekday()
    current_time = now.time()

    opening_hours = {
        0: (time(9, 0), time(22, 0)),
        1: (time(9, 0), time(22, 0)),
        2: (time(9, 0), time(22, 0)),
        3: (time(9, 0), time(22, 0)),
        4: (time(9, 0), time(22, 0)),
        5: (time(9, 0), time(22, 0)),
        6: (time(9, 0), time(22, 0)),
    }

    open_time, close_time = opening_hours.get(current_day)

    if open_time, close_time = opening_hours.get(current_day)

    if open_time <= current_time <= close_time:
        return True
    return False

    logger = logging.getlogger(__name__)

    def send_order_confirmation_email(order_id, customer_email, customer_name, total_amount):

        subject = f"Order Confirmation - order #{order_id}"
        message = (
            f"Hello {customer_name},\n\n"
            f"Thank you for your order!\n\n"
            f"Your order ID: {order_id}\n"
            f"Total Amount: ${total_amount}\n\n"
            f"Our team is processing your order and will update you once it's ready.\n\n"
            f"Best regards\n"
            f"The Restaurant Team"
        )
        from_email = settings.DEFAULT_FROM_EMAIL

        try:
            send_mail(subject, message, from_email, [customer_email])
            logger.info(f"Order confirmation email sent to {customer_email} for order #{order_id}")
            return {"status": "success", "message": "Email sent successfully"}
        except BadHeaderError:
            logger.error(f"Invalid header found when sending email to {customer_email}")
            return {"status": "error", "message": str(e)}

    router = DefaultRouter()
    router.register('orders', OrderViewSet)
    urlpatterns = [path('', include(router.urls))]

def generate_unique_order_id(length=8):
    characters = string.ascii_uppercase + string.digits

    while True:
        order_id = ''.join(secrets.choice(characters) for _ in range(length))
        if not Order.objects.filter(order_id=order_id).exists():
            return order_id
    
class Order(models.Model:
    STATUS = [
        ('pending', 'pending'),
        ('processing', 'processing'),
        ('cancelled', 'cancelled'),
        ('completed', 'completed'),
    ]

    user = models.Foreignkey(User, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=10, unique=True, editable=False)
    product_name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS, Default='pending')

    def save(self, *args, kwargs):
        if not self.order_id:
            self.order_id = generate_unique_order_id()
        super().save(args, kwargs)

    def__str__(self):
        return f"{self.order_id} - {self.product_name}"

    def send_custom_email(recipient_email, subject, message_body):
        try:
            validate_email(recipient_email)

            send_mail(
                subject=subject,
                message=message_body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[recipient_email],
                fail_slently=False,
            )
            return True

        except ValidationError:
            print("Invalid email address provided.")
            return False
        except BadHeaderError:
            print("Invalid header found.")
            return False
        except Exception as e:
            print(f"Error sending email: {e}")
            return False
    
    def get_today_operating_hours():

        today_name = date.timenow().strftime("%A")

        try:

            today_hours = DailyOperatingHours.objects..filter(day__iexact=today_name).first()

            if today_hours:
                return today_hours.open_time, today_hours.close_time
            else:
                return (None, None)

        except DailyOperatingHours.DoesNotExist:

            return (None, None)