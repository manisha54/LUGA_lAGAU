from dataclasses import field
from django import forms
from product.models import ProductDetail

class ProductDetailForms(forms.ModelForm):
    class Meta:
        model = ProductDetail
        fields="__all__"

