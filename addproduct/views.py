from django.shortcuts import render ,redirect
from addproduct.form import AddProductForms
from addproduct.models import AddProduct
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User

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
    if request.method == "POST":
        user = authenticate(request,
        username=request.POST['username'], 
        password =request.POST['password'])

        if user is not None:
            login(request,user)
            return redirect("/addproduct/create")
            pass
        else:
            messages.error(request, "invalid credential")
            return redirect("/addproduct/login")
    else:
        return render(request, 'addproduct/signin.html')

def signout(request):
    print(request.method)       
    if request.method == "POST":
        User.objects.create_user(
            first_name = request.POST['firstname'],
            last_name = request.POST['lastname'],
            email = request.POST['email'],
            username = request.POST['username'],
            password = request.POST['password'],
        )
        return redirect("/addproduct/signin")
        print(request.POST)
    else:
        return render(request, 'addproduct/signout.html')

