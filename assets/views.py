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

    data = {
        'assets':paged_assets,
    }
    return render(request,'assets/assets.html', data)

def asset_details(request,id):
    single_asset = get_object_or_404(Asset, pk=id)
    data = {
        'single_asset':single_asset,
    }
    return render(request,'assets/asset_details.html',data)


def search(request):
    assets = Asset.objects.order_by('-created_date')

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            assets = assets.filter(description__icontains=keyword)

    data = {
        'assets':assets,
    }
    return render(request,'assets/search.html',data)
