
import datetime
from email.headerregistry import Address
from multiprocessing import context
from re import template
from tkinter import E, S
from tokenize import Name
from turtle import title
from unittest import result
from django.shortcuts import render

import product
from .models import Image

# Create your views here.
def index(request):
    pics = Image.objects.all()
    return render(request, 'home/index.html',{"pics" : pics})


def search(request):
    return render(request, 'home/search.html')


def checkout(request):
    if request.method == "POST":
        Name = request.POST.get('Name')
        Phone1 = request.POST.get('Phone1')
        Email = request.POST.get('Email')
        Phone2 = request.POST.get('Phone2')
        Address = request.POST.get('Address')
        Quantity = request.POST.get('Quantity')
        P_name = request.POST.get('P_name')
        City = request.POST.get('City')
        Country = request.POST.get('Country')
        State = request.POST.get('State')
        Zipcode = request.POST.get('Zipcode')
        checkout = checkout(Name=Name,Phone1 =Phone1, Email=Email, Phone2=Phone2,Address=Address, Quantity=Quantity, P_name=P_name,City=City, Country=Country,State=State,Zipcode=Zipcode, date=datetime.today())
        checkout.save()
    return render(request, 'home/checkout.html')    


# class searchdata():
#     template_name = "search.html"
#     def get_context_data(self, **kwargs):
#         context = super(). get_context_data(**kwargs)
#         kw = self.request.GET.get['keyword']
#         results = product.objects.filter(caption=kw)        
#         context["results"] = results
#         return context

