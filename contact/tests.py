from django.test import SimpleTestCase, TestCase
from django.urls import resolve, reverse
from contact.views import edit, index,save, update



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

    # def test_edit_url(self):
    #     url = reverse('contact_edit')
    #     print(url)
    #     self.assertEquals(resolve(url).func,edit)            

    # def test_update_url(self):
    #     url = reverse('update')
    #     print(url)
    #     self.assertEquals(resolve(url).func,update)            


from django.test import TestCase,Client, SimpleTestCase
from django.contrib.auth.models import User
from contact.views import edit, index, create
from contact.models import Contact, Customer

# Create your tests here.

class testviews(TestCase):
    def test_index(self):
        user = User.objects.create(username='manisha')
        user.set_password('12345')
        user.save()
        client=Client()
        logged_in = client.login(username='manisha', password='12345')
        response=client.get(reverse(index))

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'contact/index.html')
        
    def test_create(self):
        user = User.objects.create(username='manisha')
        user.set_password('12345')
        user.save()
        client=Client()
        logged_in = client.login(username='manisha', password='12345')
        response=client.get(reverse('contact'),{
           'name' : "name",
           'email' : "email",
           'phone' : "phone",
           'decs' : "decs",
           
        })

        self.assertEquals(response.status_code,302)
        self.assertTemplateUsed(response, '/contact/index.html')

    def test_delete(self):
            client = Client()
            c = Contact.objects.create(
            name = "name",
            email = "email",
            phone = "phone",
            decs = "decs",
          
            )
            print('this')
            print(c.contact)
            response=client.delete(reverse('contact_delete',args=[2]))
            self.assertEquals(response.status_code, 302)