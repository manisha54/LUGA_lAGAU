from django.urls import path
from contact import views
urlpatterns =[
    path("",views.index,name="contact"),
    path("/contact",views.contactus),

    
    path("/save",views.save, name='contact_save'),
    path("/index",views.index, name="index"),
    path("/edit/<int:id>",views.edit, name='contact_edit'),
    path("/update/<int:id>",views.update),
    path("/delete/<int:id>",views.delete),
]