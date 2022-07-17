from django.urls import path
from customer import views
urlpatterns =[
  
    path("/customer",views.index),
    path("create",views.create, name='customer_create'),
  
]