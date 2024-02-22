from django import forms
from django.forms import modelformset_factory
from .models import *


class GeneralBuluntuForm(forms.ModelForm):
    class Meta:
        model = SetGeneralBuluntu
        fields = "__all__"
        exclude = ["processedBy"]


"""AŞAĞIDAKI FORMLAR DENEYSELDİR."""

"""
class RelatedGenelForm(forms.ModelForm):

    class Meta:
        model = RelatedGenelField
        fields = "__all__"
        exclude = ["form"]

class RelatedBezemesgKeyForm(forms.ModelForm):

    class Meta:
        model = RelatedBezemesgKey
        fields= "__all__"
        exclude = ["form"]

"""