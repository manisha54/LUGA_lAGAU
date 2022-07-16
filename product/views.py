from django.shortcuts import render
from flask import redirect

from product.forms import ProductDetailForms
from .models import Image, ProductDetail
# Create your views here.
def singleproduct(request):
    pics = Image.objects.all()
    return render(request, 'product/singleproduct.html',{"pics" : pics})




def index(request):
    pics = ProductDetail.objects.all()
    return render(request, 'home/singleproduct.html',{"pics" : pics})


def productdetail(request):
    return render(request, 'addproduct/productdetail.html')
   
def saveFn(request):
     print(request.FILES)
     forms=ProductDetailForms(request.POST,request.FILES)
     forms.save()
     return redirect('/')
