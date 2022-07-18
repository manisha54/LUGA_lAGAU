
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
        decs = request.POST.get('decs')
        contactus = contactus(name=name, email=email, phone=phone,decs=decs, date=datetime.today())
        contactus.save()
    return render(request, 'contact/contact.html')

def save(request):
     form = ContactForms(request.POST)
     print(request.FILES)
     form.save()
     return redirect('/contact')


def index(request):
     contact = Contact.objects.all()
     return render(request, 'contact/index.html',{ 'contact': contact})

def edit(request,id):
     print(id)
     data=Contact.objects.get(id=id)
     return render(request, "contact/edit.html",{'data': data})

def update(request,id):
     data=Contact.objects.get(id=id)
     form=ContactForms(request.POST, request.FILES, instance=data)
     form.save()
     return redirect('/contact')
     
def delete(request,id):
     data=Contact.objects.get(id=id)
     data.delete()
     return redirect('/contact')
     