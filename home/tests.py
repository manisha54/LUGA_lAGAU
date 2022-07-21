from django.urls import resolve, reverse
from django.test import SimpleTestCase, TestCase

from home.views import index

# Create your tests here.
class TestUrls(SimpleTestCase):

    def test_index_url(self):
        url = reverse('home')
        print(url)
        self.assertEquals(resolve(url).func,index)
