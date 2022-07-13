from django.contrib import admin

from home.views import checkout
from .models import  Image ,Checkout
# Register your models here.

admin.site.register(Image)
admin.site.register(Checkout)