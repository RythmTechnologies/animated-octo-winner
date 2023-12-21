from django import forms
from django.forms import DateInput
from ckeditor.widgets import CKEditorWidget
from .models import *

class CustomDateInput(DateInput):
    input_type = 'date'


# CKEDITOR BAKILACAK!
class FixtureForm(forms.ModelForm):
    
    fixtureDescription = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Fixture
        fields = "__all__"
        exclude = ['user']
        widgets = {
            'dateofaddition': CustomDateInput(),
        }
    def __init__(self, *args, **kwargs):
        super(FixtureForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            # Tüm alanlara form-control sınıfını ekler
            if field_name == 'dateofaddition':
                field.widget.attrs['input_type'] = 'date'
            field.widget.attrs['class'] = 'form-control mb-3 rounded'
            
            # Alan adına göre etiket ekler
            field.widget.attrs['placeholder'] = field.label

            if field_name == "totalprice":
                field.widget.attrs['input_type'] = 'number'
                field.widget.attrs['disabled'] = True

            if field_name == "companyAddress":
                field.widget.attrs['style'] = "height: 124px;"




# set general buluntu form field

class GeneralBuluntuForm(forms.ModelForm):

    class Meta:
        model = SetGeneralBuluntu
        fields = "__all__"
        exclude  = ['user']

# ends