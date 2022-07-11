from django.shortcuts import render
from .models import Image
# Create your views here.
def singleproduct(request):
    pics = Image.objects.all()
    return render(request, 'product/singleproduct.html',{"pics" : pics})




