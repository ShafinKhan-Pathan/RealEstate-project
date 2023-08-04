from django.shortcuts import render,redirect
from assets.models import Asset
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contacts.models import Contact
from django.contrib.auth.decorators import login_required


# Create your views here.
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
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are now logged in !')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid Login Credentials')

    return render(request,'accounts/login.html',data)
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
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username Alreadt Exists !')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Email Already Exists !')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                    auth.login(request,user)
                    messages.success(request,'You are not logged in !')
                    return redirect('dashboard')
                    user.save()
                    messages.success(request,'You Are Successfully Registered')
                    return redirect('login')

        else:
            return redirect('register')
    else:
        return render(request,'accounts/register.html',data)



def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You are logged out')
        return redirect('login')

    return redirect('home')



@login_required(login_url = 'login')
def dashboard(request):
    user_inquiry = Contact.objects.order_by('-created_date').filter(user_id=request.user.id)
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
        'inquiries':user_inquiry,
    }
    return render(request,'accounts/dashboard.html',data)
