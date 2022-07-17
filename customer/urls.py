from django.urls import path
from customer import views
urlpatterns =[

    path("",views.index),
    path("/create",views.create, name='customer_create'),
    path("/save",views.save, name='customer_save'),
]