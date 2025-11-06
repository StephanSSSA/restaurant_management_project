import string
import secrets
import re
from .models import Coupon 

def generate_coupon_code(length=10):
    characters = string.ascii_uppercase + string.digits

    while True:
        code = ''.join(secrets.choice(characters) for _ in range(length))

        if not Coupon.objects.filter(code=code).exist():
            return code

def is_valid_phone_number(phone_number):
    
    pattern = r'^\+?\d{1,3}?[-\s]?\d{10,12}$'

    if re.match(pattern, phone_number):
        return True
    else:
        return False