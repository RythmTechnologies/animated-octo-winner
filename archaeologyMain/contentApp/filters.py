import django_filters
from django import forms
from .models import Fixture, AcmaRapor, DocumentCreateModel


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
    rapordate = django_filters.DateFilter(widget=CustomDateInput())

    class Meta:
        model = AcmaRapor
        fields = [
            "title",
            "rapordetail",
            "owner",
            "rapordate",
        ]


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
    docdate = django_filters.DateFilter(widget=CustomDateInput())

    class Meta:
        model = DocumentCreateModel
        fields = ["docno", "relevantunit", "docdate", "docsubject"]
