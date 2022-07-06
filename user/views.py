
from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Create your views here.
from .forms import CreateUserForm


def register_page(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,"registered sucessfully")
            return redirect("/user/login")
    context = {'form': form}
    return render(request,"user/register.html",context)
   

def login_page(request):
    if request.method == 'POST':
        username =request.POST.get('username')
        password =request.POST.get('password')

        user =authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/home/index")
            
    context = {}
    return render(request,"user/login.html",context)




