
from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from shop.models import Category, Product


# Create your views here.
# def index(request):
#     return HttpResponse('hiiii')


def allProdCat(request, c_slug=None):
    c_page = None
    products_list = None
    products = None

    if c_slug is not None:
        c_page = get_object_or_404(Category, slug=c_slug)
        products_list = Product.objects.filter(category=c_page, available=True)
    else:
        products_list = Product.objects.filter(available=True)

    paginator = Paginator(products_list, 6)
    page = request.GET.get('page', 1)

    try:
        products = paginator.page(page)
    except (EmptyPage, PageNotAnInteger):
        products = paginator.page(1)

    return render(request, "category.html", {'category': c_page, 'products': products})

def ProDetail(request, c_slug, product_slug):
    try:
        product=Product.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'product':product})

