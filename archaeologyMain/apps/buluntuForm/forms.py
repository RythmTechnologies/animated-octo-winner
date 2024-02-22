from django import forms
from .models import *




class GeneralFieldsForm(forms.ModelForm):

    class Meta:
        model = RelatedGenelField
        fields = "__all__"

class BezemesForm(forms.ModelForm):

    class Meta:
        model = RelatedBezemes
        fields = "__all__"







"""DİNAMİK FORM YAPISI"""
class CombinedForms(forms.Form):
    

   def __init__(self, form, *args, **kwargs):
        super(CombinedForms, self).__init__(*args, **kwargs)
        print("GELEN FORM:", form.buluntu_name)
        print("INIT FORM ID:", form.related_custom_field.all())
   
        field_data = {}
        general_fields = form.related_general_field
        bezemes = form.related_bezemes_field
        # deneysel
        if bezemes.count() > 0:
              
            self.fields.update(BezemesForm().fields)
              
        
        if general_fields.count() > 0:
                self.fields.update(GeneralFieldsForm().fields)
    
    
        # DICT TEST

        """
        for i in range(3):  # Örnek olarak, 3 tane alan ekliyoruz
            field_name = f'custom_field_{i+1}'
            self.fields[field_name] = forms.CharField(label=f'Custom Field {i+1}', required=False)
        """