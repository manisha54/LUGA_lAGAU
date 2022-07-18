from django.urls import path
from customer import views
urlpatterns =[

    path("",views.index,name="customer"),
    path("/create",views.create, name='customer_create'),
    path("/save",views.save, name='customer_save'),
    path("/edit/<int:id>",views.edit, name='customer_edit'),
    path("/update/<int:id>",views.update,name='customer_update'),
    path("/delete/<int:id>",views.delete,name='customer_delete'),
]
