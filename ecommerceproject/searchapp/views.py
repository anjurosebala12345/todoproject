
from django.shortcuts import render
from shop.models import Product
from django.db.models import Q

from shop.models import Product


# Create your views here.



def SearchResult(request):
    products = None  # Use lowercase 'products' instead of 'Products'
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
    return render(request, 'search.html', {'query': query, 'products': products})