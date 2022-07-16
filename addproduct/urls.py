from django.urls import path
from addproduct import views
urlpatterns =[
    path("/signin",views.signin),
    path("/signout",views.signout),
    path("/create",views.create, name='product_create'),
    path("/save",views.saveFn, name='product_save'),
    
]
