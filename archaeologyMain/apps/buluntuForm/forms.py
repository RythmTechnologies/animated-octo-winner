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


class CustomFieldsForm(forms.ModelForm):

    class Meta:
        model = CustomFields
        fields = "__all__"
        exclude = ["linked", "field"]





"""DİNAMİK FORM YAPISI"""
class CombinedForms(forms.Form):
    

   def __init__(self, instance, *args, **kwargs):
 

        super(CombinedForms, self).__init__(*args, **kwargs)

        print("GELEN FORM:", instance.buluntu_name)

        # deneysel
        general_fields = instance.related_general_field
        bezemes = instance.related_bezemes_field
        custom_fields = instance.related_custom_field.all()
   
        self.form_classes_instances = [
            (BezemesForm, bezemes),
            (GeneralFieldsForm, general_fields)
        ]

     

        # multiple alanlar için
        for form_class, related_instance in self.form_classes_instances:
            if related_instance.count() > 0:
                instance = related_instance.first()
                form_instance = form_class(instance=instance)
                for field_name, field_value in form_instance.fields.items():
                    # falsy değerleri ortadan kaldir
                    if getattr(instance, field_name) is not None:
                        self.fields[field_name] = form_instance.fields[field_name]

 

        # ekstra alanlar için
        for custom_field in custom_fields:
            print(custom_field)
            field_name = f"custom_field_{custom_field.id}"
            self.fields[field_name] = forms.CharField(
                label=custom_field.field,
                required=False,
                initial=custom_field.fieldType,
            )




    # TODO: BU ALAN GÜCLENDİRİRLECEK VE BULUNTU ICIN TEST ALANI YAPILACAK HPESI REQUIRED FALSE OLACAK
    # DİNAMIK ALANLARIN VERITABNINA KAYIT EDILMESI
    # linkedler pop olacak 
   def update_fields(self, post_data, kucuk_buluntu):
        # Iterate through the fields and update them with new values from post_data

        custom_form = CustomFieldsForm(post_data)

        if custom_form.is_valid():

            custom_form = custom_form.save(commit=False)
            custom_form.linked = kucuk_buluntu

        else:

            print("ERRR:", custom_form.errors)

        """
        for field_name, field in self.fields.items():
            print("INSTANCE FIELD:", field_name)
            if field_name in post_data:
                # Use the field_name to set a new value
                self.fields[field_name].initial = post_data[field_name]
        """
             
        for form_class, related_instance in self.form_classes_instances:
            instance = related_instance.first()
            print("INSTANCE:", instance)
            # form_instance = form_class(instance=instance)
            # form_instance.save()