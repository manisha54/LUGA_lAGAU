from dataclasses import field
from django import forms
from addproduct.models import AddProduct

class AddProductForms(forms.ModelForm):
    class Meta:
        model = AddProduct
        fields="__all__"
