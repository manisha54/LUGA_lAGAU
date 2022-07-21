from django.test import SimpleTestCase, TestCase
from django.urls import resolve, reverse
from product.models import ProductDetail

from product.views import index, singleproduct, saveFn



# Create your tests here.
class TestUrls(SimpleTestCase):

        def test_index_url(self):
                url = reverse('singleproduct')
                print(url)
                self.assertEquals(resolve(url).func,singleproduct)






 
from django.test import TestCase,Client, SimpleTestCase
from django.contrib.auth.models import User
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
        self.assertTemplateUsed(response, 'product/index.html')
        

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
            self.assertTemplateUsed(response, '/product/create.html')

    def test_delete(self):
            client = Client()
            p = ProductDetail.objects.create(
            caption = "caption",
            price = "price",
            image = "image",
           
            )
            print('this')
            print(p.product_id)
            response=client.delete(reverse('product_delete',args=[2]))
            self.assertEquals(response.status_code, 302)               