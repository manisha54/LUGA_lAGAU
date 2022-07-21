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



from django.test import TestCase,Client, SimpleTestCase
from django.contrib.auth.models import User
from addproduct.views import index, create
from addproduct.models import AddProduct


class testviews(TestCase):
    def test_index(self):
        user = User.objects.create(username='manisha')
        user.set_password('12345')
        user.save()
        client=Client()
        logged_in = client.login(username='manisha', password='12345')
        response=client.get(reverse(index))

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'AddProduct/index.html')
        

    def test_create(self):
            user = User.objects.create(username='manisha')
            user.set_password('12345')
            user.save()
            client=Client()
            logged_in = client.login(username='manisha', password='12345')
            response=client.get(reverse('product_create'),{
            'caption' : "caption",
            'price' : "price",
            'image' : "image",
            })

            self.assertEquals(response.status_code,302)
            self.assertTemplateUsed(response, '/addproduct/create.html')

    def test_delete(self):
            client = Client()
            p = AddProduct.objects.create(
            Name = "Name",
            Phone1 = "Phone1",
            Email = "Email",
            Phone2 = "Phone2",
            Address = "Address",
            Quantity = "Quantity",
            P_name = "P_name",
            City = "City",
            Country = "Country",
            state = "state",
            zipcode = "zipcode",
            )
            print('this')
            print(p.product_id)
            response=client.delete(reverse('product_delete',args=[2]))
            self.assertEquals(response.status_code, 302)