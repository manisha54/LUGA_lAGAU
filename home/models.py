
from email.headerregistry import Address
from django.db import models

# Create your models here.
class Image(models.Model):
    caption=models.CharField(max_length=50)
    price=models.CharField(max_length=50,default="")
    image=models.FileField(upload_to="static/image/women",default="defult.jpg")

    def __str__(self):
         return self.caption



class Checkout(models.Model):
    Name = models.CharField(max_length=100)
    Phone1=models.CharField(max_length=15)
    Email=models.CharField(max_length=150)
    Phone2=models.CharField(max_length=15)   
    Address = models.TextField()
    Quantity=models.CharField(max_length=150)
    P_name=models.CharField(max_length=15) 
    City=models.CharField(max_length=150)
    Country=models.CharField(max_length=15) 
    State=models.CharField(max_length=150)
    Zipcode=models.CharField(max_length=15) 
    date =models.DateTimeField
   
    class Meta:
        db_table="checkout"

 


   