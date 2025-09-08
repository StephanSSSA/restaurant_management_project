from datetime import datetime

def site_info(request):
    
    return {
        "restaurant_name": "Spicy Food Corner",
        "Current_year": datetime.now().year,
        "opening_hours": "Mon-Fri: 11am-9pm, Sat-Sun: 10am-10pm",
    }
