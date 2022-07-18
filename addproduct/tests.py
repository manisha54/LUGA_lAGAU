from django.test import SimpleTestCase, TestCase
from django.urls import resolve, reverse
from addproduct.views import create, saveFn


# Create your tests here.
class TestUrls(SimpleTestCase):

    def test_create_url(self):
        url = reverse('product_create')
        print(url)
        self.assertEquals(resolve(url).func,create)

    def test_product_url(self):
        url = reverse('product_save')
        print(url)
        self.assertEquals(resolve(url).func,saveFn)    