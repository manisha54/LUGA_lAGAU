from email.headerregistry import Address
from django.db import models

# Create your models here.
class Customer(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True)
    Name=models.CharField(max_length=100)
    Phone1=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Phone2=models.CharField(max_length=50)
    Address=models.CharField(max_length=80)
    Quantity=models.CharField(max_length=10)
    P_name=models.CharField(max_length=50)
    City=models.CharField(max_length=60)   
    Country=models.CharField(max_length=80) 
    state=models.CharField(max_length=30) 
    zipcode=models.CharField(max_length=40) 
    class Meta:
        db_table="customer"
