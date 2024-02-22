from django.db import models



class Formlar(models.Model):
     
     buluntu_name = models.CharField(("Küçük Buluntu Adı"), max_length=50)

     class Meta:
        verbose_name = "Buluntu Form"
        verbose_name_plural = "Buluntu Formu"


     def __str__(self):
        return self.buluntu_name

""" DYNAMIC MODELS """
class RelatedGenelField(models.Model):

      piece = models.ForeignKey("buluntu.Piece", verbose_name=("Eser"), on_delete=models.CASCADE, blank = True, null = True)
      status = models.ForeignKey("buluntu.Status", verbose_name=("Durum"), on_delete=models.CASCADE, blank = True,  null = True)
      animalType = models.ForeignKey("buluntu.AnimalType", verbose_name=("Hayvan Türü"), on_delete=models.CASCADE, blank = True, null = True)
      linked = models.ForeignKey(Formlar, on_delete=models.CASCADE, related_name='related_general_field')


class RelatedBezemes(models.Model):

    bezeme = models.ForeignKey("buluntu.Bezeme", on_delete=models.CASCADE, null=True, blank=True)
    bezemeAlani = models.ForeignKey("buluntu.BezemeAlani", on_delete=models.CASCADE, null=True, blank=True)
    bezemeTuru = models.ForeignKey("buluntu.BezemeTuru", on_delete=models.CASCADE, null=True, blank=True)
    linked = models.ForeignKey(Formlar, on_delete=models.CASCADE, related_name='related_bezemes_field')


class CustomFields(models.Model):


    field = models.CharField(("Değer"), max_length=50)
    fieldType = models.CharField(("Veri"), max_length=50, default = "")
    fieldVisible = models.BooleanField(("Gösterilsin mi"), default = True)

    linked = models.ForeignKey(Formlar, on_delete=models.CASCADE, related_name='related_custom_field', null = True)

""" BASE MODELS """

class TOPRAKORNEGI(models.Model):
    piece_name = models.ForeignKey("buluntu.Piece", verbose_name=("Eser Adı"), on_delete=models.CASCADE)
    status = models.ForeignKey("buluntu.Status", verbose_name=("Durum"), on_delete=models.CASCADE)
    amount = models.CharField(("Miktar"), max_length=50)
    flotasyonOncesi = models.CharField(("Flotasyon Öncesi Miktar"), max_length=50)
    flotasyonSonrasi = models.CharField(("Flotasyon Sonrası Miktar"), max_length=50)
    description = models.TextField("Tanım")
    
    # Bu satır ile TOPRAKORNEGI modelini Formlar modeline ForeignKey ile bağlıyoruz.
    linked = models.ForeignKey(Formlar, on_delete=models.CASCADE, related_name="toprak_ornegi")



class C14(models.Model):
    C14_CHOICES = (
        ("1", "Anali Tüpü"),
        ("2", "Plastik Kutu"),
        ("3", "Korunmuş Ahşap Örneği")
    )

    piece_name = models.ForeignKey("buluntu.Piece", verbose_name=("Eser Adı"), on_delete=models.CASCADE)
    status = models.ForeignKey("buluntu.Status", verbose_name=("Durum"), on_delete=models.CASCADE)
    type = models.ForeignKey("buluntu.Tur", verbose_name=("Tür"), on_delete=models.CASCADE)
    amount = models.CharField(("Miktar"), max_length=50, choices=C14_CHOICES)
    description = models.TextField(("Tanım"))

    linked = models.ForeignKey(Formlar, on_delete=models.CASCADE, related_name="c14")
    