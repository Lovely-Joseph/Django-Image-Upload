# from dataclasses import fields
from django import forms
from .models import imageModel
# Creating forms
class ImgForm(forms.ModelForm):
    # Describing the table relation 
    class Meta:
        model=imageModel
        fields='__all__'
