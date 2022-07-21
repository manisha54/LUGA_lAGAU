
from multiprocessing.connection import Client
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

    # def test_edit_url(self):
    #     url = reverse('customer_edit')
    #     print(url)
    #     self.assertEquals(resolve(url).func,edit)

    # def test_update_url(self):
    #     url = reverse('customer_update')
    #     print(url)
    #     self.assertEquals(resolve(url).func,update)

    # def test_delete_url(self):
    #     url = reverse('customer_delete')
    #     print(url)
    #     self.assertEquals(resolve(url).func,delete)
    



# from django.test import TestCase,Client, SimpleTestCase
# from django.contrib.auth.models import User
# from customer.views import edit, index, create
# from customer.models import Customer

# # Create your tests here.

# class testviews(TestCase):
#     def test_index(self):
#         user = User.objects.create(username='manisha')
#         user.set_password('12345')
#         user.save()
#         client=Client()
#         logged_in = client.login(username='manisha', password='12345')
#         response=client.get(reverse(index))

#         self.assertEquals(response.status_code,200)
#         self.assertTemplateUsed(response, 'customer/index.html')

#     def test_create(self):
#         user = User.objects.create(username='manisha')
#         user.set_password('12345')
#         user.save()
#         client=Client()
#         logged_in = client.login(username='manisha', password='12345')
#         response=client.get(reverse('customer_create'),{
#            'Name' : "Name",
#            'Phone1' : "Phone1",
#            'Email' : "Email",
#            'Phone2' : "Phone2",
#            'Address' : "Address",
#            'Quantity' : "Quantity",
#            'P_name' : "P_name",
#            'City' : "City",
#            'Country' : "Country",
#            'state' : "state",
#            'zipcode' : "zipcode",

#         })

#         self.assertEquals(response.status_code,302)
#         self.assertTemplateUsed(response, '/customer/index.html')

#     def test_delete(self):
#         client = Client()
#         c = Customer.objects.create(
#            Name = "Name",
#            Phone1 = "Phone1",
#            Email = "Email",
#            Phone2 = "Phone2",
#            Address = "Address",
#            Quantity = "Quantity",
#            P_name = "P_name",
#            City = "City",
#            Country = "Country",
#            state = "state",
#            zipcode = "zipcode",
#         )
#         print('this')
#         print(c.customer_id)
#         response=client.delete(reverse('customer_delete',args=[2]))
#         self.assertEquals(response.status_code, 302)