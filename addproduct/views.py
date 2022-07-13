from django.shortcuts import render ,redirect
from addproduct.form import AddProductForms

from addproduct.models import AddProduct

# Create your views here.


def index(request):
    pics = AddProduct.objects.all()
    return render(request, 'home/index.html',{"pics" : pics})


def create(request):
    return render(request, 'addproduct/create.html')
   
def saveFn(request):
     print(request.FILES)
     forms=AddProductForms(request.POST,request.FILES)
     forms.save()
     return redirect('/')













def signin(request):
    return render(request, 'addproduct/signin.html')

def signout(request):
    return render(request, 'addproduct/signout.html')

