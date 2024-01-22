from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(SetGeneralBuluntu)
admin.site.register(SetColour)
admin.site.register(BuluntuAlani)
admin.site.register(BuluntuTypes)
admin.site.register(BuluntuPeriod)
admin.site.register(GeneralInstructions)
admin.site.register(BuluntuImages)
admin.site.register(MinorBuluntuForm)
admin.site.register(Pieces)
admin.site.register(AstarColour)
admin.site.register((HamurKatkiBoy, HamurKatkiTur, HamurGozeneklilik, HamurFirinlama, HamurYuzey, HamurSertlik))
admin.site.register(Bezeme)