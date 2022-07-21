from django.urls import path
from product import views

urlpatterns =[
  
    path("/product",views.singleproduct, name="singleproduct"),   
   

    path("/productdetail",views.productdetail,name="product_detail"), 
    path("/save",views.saveFn, name='product_save'), 
]