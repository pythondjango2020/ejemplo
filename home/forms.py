from django import forms
from .models import *

class forms_registro(forms.Form):
    nombre      = forms.CharField(widget=forms.TextInput())
    apellido    = forms.CharField(widget=forms.TextInput())
    identificacion = forms.CharField(widget=forms.TextInput())

