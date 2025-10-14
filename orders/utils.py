import string
import secrets
from .models import Coupon 
from datetime import date
from django.db.models import Sum
from .models import Order


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