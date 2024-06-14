from django.urls import path
from product import views

app_name = 'product'

urlpatterns = [
    
    path('search/', views.catalog, name='search'),
    path('<slug:category_slug>/', views.catalog, name='index'),
    path('product/<slug:product_slug>/', views.product, name='product'),
]