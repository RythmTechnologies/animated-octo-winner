from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(TOPRAKORNEGI)
# admin.site.register(C14)
# admin.site.register(PISMISTOPRAK)
# admin.site.register(CANAKCOMLEK)
# admin.site.register(Metal)
# admin.site.register(Tas)
# admin.site.register(KEMIK)


# STACKED / TABULAR INLINES 
class RelatedGeneraldInline(admin.StackedInline):
    verbose_name = "Genel Bilgi"
    verbose_name_plural = "Genel Bilgiler"

    model = RelatedGenelField
    extra = 0


class RelatedBezemesInline(admin.StackedInline):
    verbose_name = "Bezeme"
    verbose_name_plural = "Bezeme Bilgileri"

    model = RelatedBezemes
    extra = 0


class RelatedCustomField(admin.TabularInline):

    verbose_name = "Ekstra"
    verbose_name_plural = "Ekstra Alan"

    model = CustomFields
    extra = 0
    fields = ['field', 'fieldType', "fieldVisible"]

class FormlarAdmin(admin.ModelAdmin):
    inlines = [RelatedGeneraldInline, RelatedBezemesInline, RelatedCustomField]



admin.site.register(Formlar, FormlarAdmin)
