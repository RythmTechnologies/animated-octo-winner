from django import forms
from django.forms import DateInput

from apps.specuser.models import *
from .views import *
from .models import *


class CustomDateInput(DateInput):
    input_type = "date"


class DocumentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super(DocumentForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if field_name in [
                "incomingdoc",
                "outgoingdoc",
                "amount",
                "high",
                "middle",
                "low",
            ]:
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control mb-3 rounded"
                field.widget.attrs["placeholder"] = field.label

            if field_name == "user":
                field.initial = user
                field.disabled = True

    class Meta:
        model = DocumentCreateModel
        fields = "__all__"
        widgets = {"docdate": CustomDateInput()}
