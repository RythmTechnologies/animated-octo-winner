from django import forms
from .models import *


class GeneralBuluntuForm(forms.ModelForm):
    class Meta:
        model = SetGeneralBuluntu
        fields = "__all__"
        exclude = ["user"]


class ToprakForm(forms.ModelForm):

    class Meta:
        model = Toprak
        fields = "__all__"


class C14Form(forms.ModelForm):

    class Meta:
        model = C14
        fields = "__all__"
