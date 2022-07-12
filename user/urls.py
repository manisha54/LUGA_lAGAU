from django.urls import path
from user import views
urlpatterns =[
    path("/login",views.login_page, name="register"),
    path("/register", views.register_page,name="login"),
    path("/logout", views.logout_fn, name="logout")
]