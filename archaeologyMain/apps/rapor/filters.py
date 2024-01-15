import django_filters
from django import forms
from .models import AcmaRapor
from apps.specuser.models import *


class CustomDateInput(forms.DateInput):
    input_type = "date"


class RaporAcmaFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Başlık"}
        ),
        lookup_expr="icontains",
    )
    rapordetail = django_filters.CharFilter(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Rapor Detayları"}
        ),
        lookup_expr="icontains",
    )
    owner = django_filters.CharFilter(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Formu Dolduran"}
        ),
        lookup_expr="icontains",
    )
    rapordate = django_filters.DateFilter(widget=CustomDateInput(attrs={"class":"form-control"}))

    class Meta:
        model = AcmaRapor
        fields = [
            "title",
            "rapordetail",
            "owner",
            "rapordate",
        ]