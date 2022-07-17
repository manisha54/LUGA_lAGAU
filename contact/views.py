
from django.shortcuts import redirect, render
from datetime import datetime
from contact.forms import ContactForms
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

def save(request):
     form = ContactForms(request.POST)
     print(request.FILES)
     form.save()
     return redirect('/contact')
