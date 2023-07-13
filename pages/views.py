from django.shortcuts import render
from .models import Team

# Create your views here.

def home(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request,'pages/home.html',data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams':teams,
    }
    return render(request,'pages/about.html',data)

def property(request):
    return render(request,'pages/property.html')

def contact(request):
    return render(request,'pages/contact.html')
