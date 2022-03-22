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
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/detail.html', {'product': product})


def category_list(request, category_slug):
    "View for categories location"
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/category.html', {'category': category, 'products': products})
