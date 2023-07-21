from django.urls import path
from .import views

urlpatterns = [
    path('', views.assets,name="assets"),
    path('<int:id>', views.asset_details , name="asset_details"),
]
