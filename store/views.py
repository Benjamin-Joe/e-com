"Store views"
from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def categories(request):
    "View for displaing categories in dropdown list"
    return{'categories': Category.objects.all()}


def all_products(request):
    "View for all of the store's products"
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})


def product_detail(request, slug):
    "View for individual product details"
    product = get_object_or_404(Product, slug=slug)