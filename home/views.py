
from multiprocessing import context
from re import template
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


# class searchdata():
#     template_name = "search.html"
#     def get_context_data(self, **kwargs):
#         context = super(). get_context_data(**kwargs)
#         kw = self.request.GET.get['keyword']
#         results = product.objects.filter(caption=kw)        
#         context["results"] = results
#         return context

