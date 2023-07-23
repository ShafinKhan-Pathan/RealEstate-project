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
    #search_fields = Asset.objects.values('type','city','bed','garage','bath','price')
    type_search = Asset.objects.values_list('type', flat=True).distinct()
    city_search = Asset.objects.values_list('city', flat=True).distinct()
    bed_search = Asset.objects.values_list('bed', flat=True).distinct()
    garage_search = Asset.objects.values_list('garage', flat=True).distinct()
    bath_search = Asset.objects.values_list('bath', flat=True).distinct()
    price_search = Asset.objects.values_list('price', flat=True).distinct()
    year_search = Asset.objects.values_list('year', flat=True).distinct().order_by('-year')
    data = {
        'teams': teams,
        'featured_assets':featured_assets,
        'all_assets':all_assets,
        'intro_assets':intro_assets,
        'type_search':type_search,
        'city_search':city_search,
        'bed_search':bed_search,
        'garage_search':garage_search,
        'bath_search':bath_search,
        'price_search':price_search,
        'year_search':year_search,

    }
    return render(request,'pages/home.html',data)

def about(request):
    teams = Team.objects.all()
    type_search = Asset.objects.values_list('type', flat=True).distinct()
    city_search = Asset.objects.values_list('city', flat=True).distinct()
    bed_search = Asset.objects.values_list('bed', flat=True).distinct()
    garage_search = Asset.objects.values_list('garage', flat=True).distinct()
    bath_search = Asset.objects.values_list('bath', flat=True).distinct()
    price_search = Asset.objects.values_list('price', flat=True).distinct()
    year_search = Asset.objects.values_list('year', flat=True).distinct().order_by('-year')
    data = {
        'teams':teams,
        'type_search':type_search,
        'city_search':city_search,
        'bed_search':bed_search,
        'garage_search':garage_search,
        'bath_search':bath_search,
        'price_search':price_search,
        'year_search':year_search,
    }
    return render(request,'pages/about.html',data)

def contact(request):
    type_search = Asset.objects.values_list('type', flat=True).distinct()
    city_search = Asset.objects.values_list('city', flat=True).distinct()
    bed_search = Asset.objects.values_list('bed', flat=True).distinct()
    garage_search = Asset.objects.values_list('garage', flat=True).distinct()
    bath_search = Asset.objects.values_list('bath', flat=True).distinct()
    price_search = Asset.objects.values_list('price', flat=True).distinct()
    year_search = Asset.objects.values_list('year', flat=True).distinct().order_by('-year')
    data = {
        'type_search':type_search,
        'city_search':city_search,
        'bed_search':bed_search,
        'garage_search':garage_search,
        'bath_search':bath_search,
        'price_search':price_search,
        'year_search':year_search,
    }
    return render(request,'pages/contact.html',data)

def services(request):
    type_search = Asset.objects.values_list('type', flat=True).distinct()
    city_search = Asset.objects.values_list('city', flat=True).distinct()
    bed_search = Asset.objects.values_list('bed', flat=True).distinct()
    garage_search = Asset.objects.values_list('garage', flat=True).distinct()
    bath_search = Asset.objects.values_list('bath', flat=True).distinct()
    price_search = Asset.objects.values_list('price', flat=True).distinct()
    year_search = Asset.objects.values_list('year', flat=True).distinct().order_by('-year')
    data = {
        'type_search':type_search,
        'city_search':city_search,
        'bed_search':bed_search,
        'garage_search':garage_search,
        'bath_search':bath_search,
        'price_search':price_search,
        'year_search':year_search,
    }
    return render(request,'pages/services.html',data)

def login(request):
    type_search = Asset.objects.values_list('type', flat=True).distinct()
    city_search = Asset.objects.values_list('city', flat=True).distinct()
    bed_search = Asset.objects.values_list('bed', flat=True).distinct()
    garage_search = Asset.objects.values_list('garage', flat=True).distinct()
    bath_search = Asset.objects.values_list('bath', flat=True).distinct()
    price_search = Asset.objects.values_list('price', flat=True).distinct()
    year_search = Asset.objects.values_list('year', flat=True).distinct().order_by('-year')
    data = {
        'type_search':type_search,
        'city_search':city_search,
        'bed_search':bed_search,
        'garage_search':garage_search,
        'bath_search':bath_search,
        'price_search':price_search,
        'year_search':year_search,
    }
    return render(request,'pages/login.html',data)

def register(request):
    type_search = Asset.objects.values_list('type', flat=True).distinct()
    city_search = Asset.objects.values_list('city', flat=True).distinct()
    bed_search = Asset.objects.values_list('bed', flat=True).distinct()
    garage_search = Asset.objects.values_list('garage', flat=True).distinct()
    bath_search = Asset.objects.values_list('bath', flat=True).distinct()
    price_search = Asset.objects.values_list('price', flat=True).distinct()
    year_search = Asset.objects.values_list('year', flat=True).distinct().order_by('-year')
    data = {
        'type_search':type_search,
        'city_search':city_search,
        'bed_search':bed_search,
        'garage_search':garage_search,
        'bath_search':bath_search,
        'price_search':price_search,
        'year_search':year_search,
    }
    return render(request,'pages/register.html',data)
