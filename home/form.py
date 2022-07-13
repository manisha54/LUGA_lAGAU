from dataclasses import field
from django import forms
from home.models import Checkout
class CheckoutForms(forms.ModelForm):
    class Meta:
        model = Checkout
        fields="__all__"
