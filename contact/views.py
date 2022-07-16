
from django.shortcuts import render
from datetime import datetime
from contact.models import Contact
# Create your views here.
def contactus(request):
    if request.method== "POST":
        name = request.POST.get('name')
        print(name)
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contactus = contactus(name=name, email=email, phone=phone,desc=desc, date=datetime.today())
        contactus.save()
    return render(request, 'contact/contact.html')


