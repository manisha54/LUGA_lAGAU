from django.test import SimpleTestCase, TestCase
from django.urls import resolve, reverse
from contact.views import edit, index,save



# Create your tests here.
class TestUrls(SimpleTestCase):

    def test_index_url(self):
        url = reverse('contact')
        print(url)
        self.assertEquals(resolve(url).func,index)

    def test_save_url(self):
        url = reverse('contact_save')
        print(url)
        self.assertEquals(resolve(url).func,save)

    def test_edit_url(self):
        url = reverse('contact_edit')
        print(url)
        self.assertEquals(resolve(url).func,edit)            
