from django.shortcuts import render, get_object_or_404
from .models import Asset
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator



# Create your views here.

def assets(request):
#Get the data from admin
    assets = Asset.objects.order_by('-created_date')
# How many number of Asset you want to show on one page
    paginator = Paginator(assets,3)
# Now we run the GET Method to get page
    page = request.GET.get('page')
# After that you will get the pages in page variable
# Now that data should now show in paged assets
    paged_assets = paginator.get_page(page)
    type_search = Asset.objects.values_list('type', flat=True).distinct()
    city_search = Asset.objects.values_list('city', flat=True).distinct()
    bed_search = Asset.objects.values_list('bed', flat=True).distinct()
    garage_search = Asset.objects.values_list('garage', flat=True).distinct()
    bath_search = Asset.objects.values_list('bath', flat=True).distinct()
    price_search = Asset.objects.values_list('price', flat=True).distinct()
    year_search = Asset.objects.values_list('year', flat=True).distinct().order_by('-year')

    data = {
        'assets':paged_assets,
        'type_search':type_search,
        'city_search':city_search,
        'bed_search':bed_search,
        'garage_search':garage_search,
        'bath_search':bath_search,
        'price_search':price_search,
        'year_search':year_search,
    }
    return render(request,'assets/assets.html', data)

def asset_details(request,id):
    single_asset = get_object_or_404(Asset, pk=id)
    type_search = Asset.objects.values_list('type', flat=True).distinct()
    city_search = Asset.objects.values_list('city', flat=True).distinct()
    bed_search = Asset.objects.values_list('bed', flat=True).distinct()
    garage_search = Asset.objects.values_list('garage', flat=True).distinct()
    bath_search = Asset.objects.values_list('bath', flat=True).distinct()
    price_search = Asset.objects.values_list('price', flat=True).distinct()
    year_search = Asset.objects.values_list('year', flat=True).distinct().order_by('-year')
    data = {
        'single_asset':single_asset,
        'type_search':type_search,
        'city_search':city_search,
        'bed_search':bed_search,
        'garage_search':garage_search,
        'bath_search':bath_search,
        'price_search':price_search,
        'year_search':year_search,
    }
    return render(request,'assets/asset_details.html',data)



def search(request):
    assets = Asset.objects.order_by('-created_date')

    if 'keyword' in request.GET:
        keyword = request.GET['keyword'] #shafin khan
        if keyword:
            assets = assets.filter(description__icontains=keyword)
    if 'type' in request.GET:
        type = request.GET['type'] #shafin khan
        if type:
            assets = assets.filter(type__iexact=type)
    if 'city' in request.GET:
        city = request.GET['city'] #shafin khan
        if city:
            assets = assets.filter(city__iexact=city)
    if 'bed' in request.GET:
        bed = request.GET['bed'] #shafin khan
        if bed:
            assets = assets.filter(bed__iexact=bed)
    if 'garage' in request.GET:
        garage = request.GET['garage'] #shafin khan
        if garage:
            assets = assets.filter(garage__iexact=garage)
    if 'bath' in request.GET:
        bath = request.GET['bath'] #shafin khan
        if bath:
            assets = assets.filter(bath__iexact=bath)
    if 'price' in request.GET:
        price = request.GET['price'] #shafin khan
        if price:
            assets = assets.filter(price__iexact=price)
    if 'year' in request.GET:
        year = request.GET['year'] #shafin khan
        if year:
            assets = assets.filter(year__iexact=year)


    data = {
        'assets':assets,
    }
    return render(request,'assets/search.html',data)
