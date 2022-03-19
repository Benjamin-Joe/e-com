"Model Testing"
from django.test import TestCase
from django.contrib.auth.models import User
from store.models import Category, Product


class TestCategoriesModel(TestCase):
    "Tests for category model"
    def setUp(self):
        "Set up data for category model tests"
        self.data1 = Category.objects.create(name='Test', slug='test')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), 'Test')


class TestProductModel(TestCase):
    "Tests for product model"
    def setUp(self):
        "Set up data for product model tests"
        Category.objects.create(name='Test', slug='test')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1,
                                            title='new', created_by_id=1, slug='new',
                                            price='29.99',
                                            image='nuka-girl.png')

    def test_products_model_entry(self):
        "Testing data entry for product model"
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'new')
