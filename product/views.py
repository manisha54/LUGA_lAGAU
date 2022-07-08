from django.shortcuts import render

# Create your views here.
def singleproduct(request):
    return render(request, 'product/singleproduct.html')


