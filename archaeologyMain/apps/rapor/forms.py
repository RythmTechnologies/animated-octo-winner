from apps.specuser.models import *
from django import forms
from django.forms import DateInput

from .models import *


class CustomDateInput(DateInput):
    input_type = "date"


class AcmaRaporForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super(AcmaRaporForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if field_name == "rapor_type":
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control mb-3 rounded"
                field.widget.attrs["placeholder"] = field.label

            if field_name == "user":
                field.initial = user
                field.disabled = True


    class Meta:
        model = AcmaRapor
        fields = "__all__"
        widgets = {
            "rapordate": CustomDateInput(),
            "rapor_type": forms.RadioSelect(),
            }