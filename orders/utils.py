import string
import secrets
from .models import Coupon 
from datetime import date, time
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