from django import forms
from .models import *


class GeneralBuluntuForm(forms.ModelForm):
    class Meta:
        model = SetGeneralBuluntu
        fields = "__all__"
        exclude = ["processedBy"]
        widgets = {

            'area': forms.CheckboxSelectMultiple,
            'type': forms.SelectMultiple(attrs={
                'class': 'form-select'
            })
        }


