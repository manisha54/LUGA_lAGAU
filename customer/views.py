from django.shortcuts import render, redirect
from customer.forms import CustomerForms
from customer.models import Customer

# Create your views here.
def index(request):
     customer = Customer.objects.all()
     return render(request, 'customer/index.html',{ 'customer': customer})
     
def create(request):
    return render(request, "addproduct/create.html")

def save(request):
     form = CustomerForms(request.POST)
     print(request.FILES)
     form.save()
     return redirect('/customer')
