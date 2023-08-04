from django.shortcuts import render, redirect
from .models import Team
from assets.models import Asset
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages
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
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        email_subject = 'You have new message from HomeHub'
        message_body = 'Name : ' +name+ '.Email : '+email+ '. Message : ' +message
        admin_info = User.objects.get(is_superuser = True)
        admin_email = admin_info.email
        send_mail(
            email_subject,
            message_body,
            "testingprojectdjango@gmail.com",
            [admin_email],
            fail_silently=False,
        )
        messages.success(request,'Thank you for contacting us. We will get back to you shortly.')
        return redirect('contact')
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
def allteam(request):
    teams = Team.objects.all()
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
        'type_search':type_search,
        'city_search':city_search,
        'bed_search':bed_search,
        'garage_search':garage_search,
        'bath_search':bath_search,
        'price_search':price_search,
        'year_search':year_search,

    }
    return render(request,'pages/allteam.html',data)
