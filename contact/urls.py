from django.urls import path
from contact import views
urlpatterns =[
    path("",views.contactus,name="contact"),
    path("/contact",views.contactus),
    path("/save",views.save, name='customer_save'),
]