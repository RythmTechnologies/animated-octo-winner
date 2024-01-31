from django import forms
from .models import *


class GeneralBuluntuForm(forms.ModelForm):
    class Meta:
        model = SetGeneralBuluntu
        fields = "__all__"
        exclude = ["user"]

"""
class ToprakForm(forms.ModelForm):

    class Meta:
        model = Toprak
        fields = "__all__"


class C14Form(forms.ModelForm):

    class Meta:
        model = C14
        fields = "__all__"


class PismikToprakForm(forms.ModelForm):
        class Meta:
            model = PismisToprak
            fields = "__all__"

"""


class ToprakForm(forms.ModelForm):

    class Meta:
        model = Test
        fields = ["piece", "status", "amount", "flotasyonBefore", "flotasyonAfter", "defination"]


class C14Form(forms.ModelForm): 
    class Meta: 
        model = Test
        fields = ["piece", "status", "type", "c14_choices", "defination"]

class PismikToprakForm(forms.ModelForm):
        class Meta:
            model = Test
            fields = [
                      "piece", "status", "width", "height", "length", "size", 
                      "diameter", "weight", "disAstar", "icAstar", "hamurRenk",
                      "katki", "gozeneklik", "sertlik", "firinlama", "katkiTur",
                      "yuzeyUygulamari", "bezeme", "bezemeAlani", "bezemeTuru", 
                      "defination"
                      ]
            
class KemikForm(forms.ModelForm):
             
        class Meta:
            model = Test
            fields = ["piece", "status", "animalType", "width", "height", "length", "size", "diameter", "weight", 
                      "bezeme", "bezemeAlani", "bezemeTuru", "defination"
                     ]
            

class CanakComlekForm(forms.ModelForm):
     
        class Meta:
            model = Test
            fields = ["piece", "status", "yapimTeknik", "agizCap", "kaideDip", "govdeGenislik", "kulpGenislik", "cidarKalinlik", 
                      "disAstar", "icAstar", "hamurRenk", "katki", "gozeneklik", "sertlik", "firinlama", "katkiTur",
                      "yuzeyUygulamari", "bezeme", "bezemeAlani", "bezemeTuru"
                     ]
            
