

from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Cart(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
   
    product_qty = models.IntegerField(null=False, blank=False)
    class Meta:
        db_table="cart"

class Image(models.Model):
    caption=models.CharField(max_length=50)
    caption2=models.CharField(max_length=50,default="")
    decs = models.TextField(max_length=200,default="")
    image=models.FileField(upload_to="static/image/background",default="defult.jpg")

    def __str__(self):
         return self.caption
 