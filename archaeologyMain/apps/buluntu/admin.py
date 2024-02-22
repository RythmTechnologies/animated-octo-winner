from django.contrib import admin
from .forms import *
from .models import *
from django.forms import Media

# Register your models here.

admin.site.register(SetGeneralBuluntu)
admin.site.register(SetColour)
admin.site.register(BuluntuAlani)
admin.site.register(BuluntuTypes)
admin.site.register(BuluntuPeriod)


admin.site.register((Piece, Status, Tur, AnimalType, YapimTeknik, DisAstar, IcAstar, HamurRenk))
admin.site.register((KatkiBoyut, Gozeneklilik, Sertlik, Firinlama, KatkiTur, YuzeyUygulamalari, Bezeme, BezemeAlani, BezemeTuru))

"""ADMIN INLINE MODELS"""
# genel bilgiler

"""
class RelatedGeneraldInline(admin.StackedInline):
    verbose_name = "Genel Bilgi"
    verbose_name_plural = "Genel Bilgiler"

    model = RelatedGenelField
    extra = 0

# custom inputs
class RelatedFieldInline(admin.TabularInline):
    verbose_name = "Ek Alan"
    verbose_name_plural = "Ek Alanlar"

    model = RelatedField
    extra = 1
    fields = ['fieldName', 'fieldType']


# dropdownlar
class RelatedDropDownInline(admin.StackedInline):
    verbose_name = "Seçilebilir"
    verbose_name_plural = "Seçilebilir Alan"

    model = RelatedDropDown
    extra = 0


# foreinkeyler
class RelatedBezemesInline(admin.StackedInline):
    verbose_name = "Bezeme"
    verbose_name_plural = "Bezeme Bilgileri"

    model = RelatedBezemesgKey
    extra = 0

# hamur özellikleri
class RelatedHamursInline(admin.StackedInline):
    verbose_name = "Hamur Özelliği"
    verbose_name_plural = "Hamur Özellikleri"
    
    model = RelatedHamurKey
    extra = 0

# ic/dıs astar
class RelatedRenkInline(admin.StackedInline):
    verbose_name = "Renk Özelliği"
    verbose_name_plural = "Renk Özellikleri"
    
    model = RelatedRenk
    extra = 0

# combine et
class FormlarAdmin(admin.ModelAdmin):
    inlines = [RelatedGeneraldInline, RelatedFieldInline, RelatedBezemesInline, RelatedRenkInline, RelatedHamursInline, RelatedDropDownInline]


admin.site.register(Formlar, FormlarAdmin)

"""
