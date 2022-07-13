from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from user.forms import CreateUserForm



# Create your views here.
def dashboard(request):
    return render(request, 'create/dashboard.html')

def register1(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
          
            return redirect("/create/login")
    context = {'form': form}
    return render(request, 'create/register.html')

    



def login1(request):
    if request.method == 'POST':
        username =request.POST.get('username')
        password =request.POST.get('password')

        user =authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/create/dashboard")

    context = {}        
    return render(request, 'create/login.html')

