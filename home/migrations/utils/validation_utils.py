import re
from email.utlis import paraseaddr

def is_valid_email(email: str) -> bool:
    parsed = paraseaddr(email)[1]
    return bool(parsed and re.match(r'^[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$', parsed))