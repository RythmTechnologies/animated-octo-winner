from django.contrib import admin
from .forms import *
from .models import *


# Register your models here.
admin.site.register(SetGeneralBuluntu)
admin.site.register(SetColour)
admin.site.register(BuluntuAlani)
admin.site.register(BuluntuTypes)
admin.site.register(BuluntuPeriod)


admin.site.register((Piece, Status, Tur, AnimalType, YapimTeknik, DisAstar, IcAstar, HamurRenk))
admin.site.register((KatkiBoyut, Gozeneklilik, Sertlik, Firinlama, KatkiTur, YuzeyUygulamalari, Bezeme, BezemeAlani, BezemeTuru))
