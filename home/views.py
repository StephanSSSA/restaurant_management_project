import datetime
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.db import DatabaseError
from .Models import MenuItem

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
    return render(request, "home/home.html", {
        "restuarant_name": settings.RESTARUNT_NAME,
        "current_year": datetime.today().year,
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

