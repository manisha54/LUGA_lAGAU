from django.shortcuts import render

from customer.models import Customer

# Create your views here.
def index(request):
     customer = Customer.objects.all()
     return render(request, 'customer/index.html',{ 'customer': customer})
     
def create(request):
    return render(request, "addproduct/create.html")
