from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('allproducts/', views.allProdCat, name='allProdCat'),
    path('', views.allProdCat, name='shopallProdCat'),
    path('<slug:c_slug>/', views.allProdCat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='prodCatdetail'),
]
