from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    "Category model to sort products"
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        "Meta class for category spelling in admin"
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        "Returns the category url"
        return reverse('store:category_list', args=[self.slug])

    def __str__(self):
        "Returns the category name"
        return self.name


class Product(models.Model):
    "Model for individual products in the store"
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product')
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, default='Klara Thunberg')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=200)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    rating = models.DecimalField(
                                max_digits=6, decimal_places=2,
                                null=True, blank=True)

    class Meta:
        "To arrange via date created"
        ordering = ('-created',)

    def get_absolute_url(self):
        "Getting individual product url"
        return reverse('store:product_detail', args=[self.slug])

    def __str__(self):
        "Returns the name of the product"
        return self.title
