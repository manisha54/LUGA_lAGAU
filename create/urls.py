from django.urls import path
from create import views
urlpatterns =[
    path("/login",views.login1, name="login"),
    path("/register",views.register1, name="register"),
    path("/dashboard",views.dashboard, name="dashboard"),
   
]