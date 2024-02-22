from django import forms
from django.forms import modelformset_factory
from .models import *


class GeneralBuluntuForm(forms.ModelForm):
    class Meta:
        model = SetGeneralBuluntu
        fields = "__all__"
        exclude = ["processedBy"]


