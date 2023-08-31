from django import forms 
from .models import *

class uform(forms.ModelForm):
   class Meta:
      model = Books
      fields="__all__"