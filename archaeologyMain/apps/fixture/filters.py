import django_filters
from django import forms
from .models import Fixture


class CustomDateInput(forms.DateInput):
    input_type = "date"

    def __init__(self, **kwargs):
        kwargs["attrs"] = {"class": "form-control"}
        super(CustomDateInput, self).__init__(**kwargs)


class FixtureFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Demirbaş Adı"}
        ),
        lookup_expr="icontains",
    )
    marka = django_filters.CharFilter(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Demirbaş Marka"}
        ),
        lookup_expr="icontains",
    )
    model = django_filters.CharFilter(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Demirbaş Model"}
        ),
        lookup_expr="icontains",
    )

    piece = django_filters.CharFilter(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Demirbaş Adet"}
        ),
        lookup_expr="icontains",
    )

    custodian = django_filters.CharFilter(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Zimmetli Kişi"}
        ),
        lookup_expr="icontains",
    )

    rapordate = django_filters.DateFilter(widget=CustomDateInput())

    class Meta:
        model = Fixture
        fields = [
            "name",
            "marka",
            "model",
            "piece",
            "custodian",
        ]