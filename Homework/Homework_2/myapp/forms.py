import datetime

from django import forms


class Product_form(forms.Form):
    id = forms.IntegerField()
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=300)
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    count = forms.IntegerField()
    image = forms.ImageField()
