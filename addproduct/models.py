from django.db import models

# Create your models here.
class AddProduct(models.Model):
    caption=models.CharField(max_length=50)
    price=models.CharField(max_length=50,default="")
    image=models.FileField(upload_to="static/image/women",default="defult.jpg")

    class Meta:
        db_table="AddProduct"


class SingleProduct(models.Model):
    caption=models.CharField(max_length=50)
    caption2=models.CharField(max_length=50,default="")
    decs = models.TextField(max_length=200,default="")
    image=models.FileField(upload_to="static/image/background",default="defult.jpg")

    class Meta:
        db_table="SingleProduct"
