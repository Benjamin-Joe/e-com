"Store views"
from django.shortcuts import render
from .models import Category, Product


def all_products(request):
    "View for all of the store's products"
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})
