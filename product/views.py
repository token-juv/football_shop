from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, get_object_or_404, render
from product.models import Products

from product.utils import q_search

def catalog (request, category_slug = None):


    page= request.GET.get('page', 1)
    on_sale= request.GET.get('on_sale', None)
    order_by= request.GET.get('order_by', None)
    query= request.GET.get('q', None)

    if category_slug == "all":
        product = Products.objects.all()
    elif query:
        product = q_search(query)
    else:
        product = get_list_or_404 (Products.objects.filter(category__slug=category_slug))

    if on_sale:
        product=product.filter(discount__gt=0)
        
    if order_by and order_by !="default":
        product=product.order_by(order_by)
    
        
    paginator = Paginator(product, 2)
    current_page = paginator.page(int(page))
    
    context = {
        'title': 'Store - Katalog', 
        
        'products': current_page, 
        'slug_url': category_slug
    }

    return render(request, 'product/catalog.html', context)




def product (request, product_slug):   
    
    product=Products.objects.get(slug=product_slug)
    
    context = {
    
    'product': product, 

    }
    return render(request, 'product/product.html', context=context)