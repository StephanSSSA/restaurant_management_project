from django.conf import settings
from django.shortcuts import render

def index(request):
    restarunt_name = settings.RESTARUNT_NAME
    return render(request, 'home/index.html',{"restarunt_name": restarunt_name})
def about(request):
    return render(request, "about.html")
def contact(request):
    return render(request, "home/contact.html")
def home(request):
    phone_number = settings.RESTARUNT_PHONE
    return render(request, "home.html", {"phone_number": phone_number})

