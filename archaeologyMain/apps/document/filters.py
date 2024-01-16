import django_filters
from django import forms
from .models import DocumentCreateModel


class CustomDateInput(forms.DateInput):
    input_type = "date"


class DocumentFilter(django_filters.FilterSet):
    docno = django_filters.CharFilter(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Evrak No"}
        ),
        lookup_expr="icontains",
    )
    relevantunit = django_filters.CharFilter(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "İlgili Birim"}
        ),
        lookup_expr="icontains",
    )
    docsubject = django_filters.CharFilter(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Evrak Konusu"}
        ),
        lookup_expr="icontains",
    )
    docdate = django_filters.DateFilter(widget=CustomDateInput(attrs={"class": "form-control"}))

    class Meta:
        model = DocumentCreateModel
        fields = ["docno", "relevantunit", "docdate", "docsubject"]
