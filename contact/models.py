
from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email=models.CharField(max_length=150)
    phone=models.CharField(max_length=15)
    decs = models.TextField()
    date = models.DateField

    class Meta:
        db_table="contact"

