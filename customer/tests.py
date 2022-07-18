
from django.urls import resolve, reverse
from django.test import SimpleTestCase, TestCase
from customer.views import index, create,save,edit,delete,update

# Create your tests here.
class TestUrls(SimpleTestCase):

    def test_index_url(self):
        url = reverse('customer')
        print(url)
        self.assertEquals(resolve(url).func,index)

    def test_create_url(self):
        url = reverse('customer_create')
        print(url)
        self.assertEquals(resolve(url).func,create)

    def test_save_url(self):
        url = reverse('customer_save')
        print(url)
        self.assertEquals(resolve(url).func,save)

    def test_edit_url(self):
        url = reverse('customer_edit')
        print(url)
        self.assertEquals(resolve(url).func,edit)

    def test_update_url(self):
        url = reverse('customer_update')
        print(url)
        self.assertEquals(resolve(url).func,update)

    def test_delete_url(self):
        url = reverse('customer_delete')
        print(url)
        self.assertEquals(resolve(url).func,delete)
    