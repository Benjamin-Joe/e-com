from unittest import skip
from django.test import TestCase
from django.contrib.auth.models import User
from store.models import Category, Product

from django.test import Client

def test_homepage_url(self):
    "Test homepage response status"
    response = self.Client.get('/')


class TestViewResponses(TestClient):
    def setUp(self):
        self.c = Client()

    def test_url_allowed