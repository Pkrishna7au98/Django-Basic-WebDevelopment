from django.shortcuts import render

# Create your views here
from .models import Destination


def index(request):

    dests = Destination.objects.all()

    return render(request, 'index.html', {'dests':dests})

def logo(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'base.html')

def news(request):
    return render(request, 'register.html')

def contact(request):
    return render(request, 'login.html')