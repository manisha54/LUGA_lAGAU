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

def edit(request,id):
     print(id)
     data=Customer.objects.get(id=id)
     return render(request, "customer/edit.html",{'data': data})

def update(request,id):
     data=Customer.objects.get(id=id)
     form=CustomerForms(request.POST, request.FILES, instance=data)
     form.save()
     return redirect('/customer')
     
def delete(request,id):
     data=Customer.objects.get(id=id)
     data.delete()
     return redirect('/customer')
