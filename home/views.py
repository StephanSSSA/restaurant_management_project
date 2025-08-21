from django.conf import settings
from django.shortcuts import render

def index(request):
    restarunt_name = settings.RESTARUNT_NAME
    return render(request, 'home/index.html',{"restarunt_name": restarunt_name})
def about(request):
    return render(request, "about.html")


