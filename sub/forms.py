from django import forms
from .models import *
class AdoptForm(forms.Form):
   name = forms.CharField(max_length=100)
   email = forms.EmailField(max_length=100)
   phone = forms.CharField(max_length=10)
   mes = forms.CharField(max_length=200)
   doc = forms.CharField(max_length=30)
   pictures = forms.ImageField()


