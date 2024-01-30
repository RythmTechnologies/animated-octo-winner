from django.contrib import admin
from .models import FormField

@admin.register(FormField)
class FormFieldAdmin(admin.ModelAdmin):
    list_display = ['field_name', 'display_label', 'field_type', 'required']