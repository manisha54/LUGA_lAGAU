from django.test import TestCase
from django.urls import resolve, reverse

from product.views import saveFn

# Create your tests here.
def test_save_url(self):
        url = reverse('product_save')
        print(url)
        self.assertEquals(resolve(url).func,saveFn)    