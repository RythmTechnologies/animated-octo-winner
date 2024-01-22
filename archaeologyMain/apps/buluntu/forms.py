from django import forms

from .models import SetGeneralBuluntu, GeneralInstructions, BuluntuImages, MinorBuluntu, MinorBuluntuForm


class GeneralBuluntuForm(forms.ModelForm):
    class Meta:
        model = SetGeneralBuluntu
        fields = "__all__"
        exclude = ["user"]


class GeneralInstructionsForm(forms.ModelForm):
    class Meta:
        model = GeneralInstructions
        fields = "__all__"


class BuluntuImagesForm(forms.ModelForm):
    class Meta:
        model = BuluntuImages
        fields = "__all__"
        exclude = ["buluntu"]


class MinorBuluntu(forms.ModelForm):
    class Meta:
        model = MinorBuluntu
        fields = "__all__"
        exclude = ["processedBy"]


class FinalBuluntuForm(forms.ModelForm):
    # piece = forms.ChoiceField(choices=Pieces.objects.values_list())
    class Meta:
        model = MinorBuluntuForm
        fields = "__all__"