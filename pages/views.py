from django.shortcuts import render
from .models import Team
from assets.models import Asset

# Create your views here.

def home(request):
    teams = Team.objects.all()
    featured_assets = Asset.objects.order_by('-created_date').filter(is_featured=True)
    all_assets = Asset.objects.order_by('created_date')
    intro_assets = Asset.objects.all()
    # order_by('-created_date').filter(is_featured=True)
    data = {
        'teams': teams,
        'featured_assets':featured_assets,
        'all_assets':all_assets,
        'intro_assets':intro_assets,
        #'search_fields':search_fields,

    }
    return render(request,'pages/home.html',data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams':teams,
    }
    return render(request,'pages/about.html',data)

def contact(request):
    return render(request,'pages/contact.html')

def services(request):
    return render(request,'pages/services.html')
