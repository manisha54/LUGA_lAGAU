
from django.db import models

# Create your models here.
class Image(models.Model):
    caption=models.CharField(max_length=50)
    price=models.CharField(max_length=50,default="")
    image=models.FileField(upload_to="static/image/women",default="defult.jpg")

    def __str__(self):
         return self.caption


   