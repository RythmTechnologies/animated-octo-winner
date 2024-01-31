from django import forms
from .models import FormField
from apps.specuser.models import SiteUser

class DynamicForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(DynamicForm, self).__init__(*args, **kwargs)
        for field in FormField.objects.all():
            if field.field_type == 'char':
                self.fields[field.field_name] = forms.CharField(label=field.display_label, required=field.required)
            elif field.field_type == 'email':
                self.fields[field.field_name] = forms.EmailField(label=field.display_label, required=field.required)
            elif field.field_type == 'integer':
                self.fields[field.field_name] = forms.IntegerField(label=field.display_label, required=field.required)
            elif field.field_type == 'boolean':
                self.fields[field.field_name] = forms.BooleanField(label=field.display_label, required=field.required)
            elif field.field_type == 'foreign':
                # Kullanıcı modeli için bir ModelChoiceField oluştur
                self.fields[field.field_name] = forms.ModelChoiceField(
                    queryset=SiteUser.objects.all(),
                    label=field.display_label,
                    required=field.required
                )