import datetime
import string

from apps.specuser.models import SiteUser
from colorfield.fields import ColorField
from django.db import models



"""
Aşağıdaki modeller buluntu kayıt form genel bilgiler'i kapsar
"""


# util functions
def avaiable_years():
    return [(y, y) for y in range(1991, datetime.date.today().year + 1)]


def current_year():
    return datetime.date.today().year


# PLANKARE X
def generate_letters():
    combinations = []
    alphabet = string.ascii_uppercase

    for first_char in alphabet:
        combinations.append(first_char)

    else:
        for first_char in alphabet:
            for second_char in alphabet:
                current_combination = first_char + second_char
                combinations.append(current_combination)

                # AZ'ye ulaştıysak işlemi durdur
                if current_combination == "AZ":
                    return [(char, char) for char in combinations]

        return combinations


# PLANKARE Y
def generate_numbers():
    return [(number, number) for number in range(1, 101)]


# end of util functions


"""
BuluntuTypes => Keramik, Kemik, taş, kücüktas vs.
"""


class BuluntuTypes(models.Model):
    buluntu = models.CharField(("Buluntu Türü"), max_length=40, unique=True)

    def __str__(self) -> str:
        return self.buluntu


"""
BuluntuAlani => Pulluk, Çukur, Yapı İçi vs.
"""
class BuluntuAlani(models.Model):
    alan = models.CharField(("Alan"), max_length=50)

    def __str__(self) -> str:
        return self.alan


"""
Buluntu Dönemi Burada Ayarlanır
"""


class BuluntuPeriod(models.Model):
    period = models.CharField(("Dönem"), max_length=50)

    def __str__(self) -> str:
        return self.period


"""Renk Ekleme Model"""


class SetColour(models.Model):
    colorName = models.CharField(("Renk Adı"), max_length=20, default = "Kırmızı")
    color = ColorField(default="#FF0000", verbose_name="Renk Kodu", unique=True)

    def __str__(self) -> str:
        return self.colorName


"""buluntu ekle modeli"""

class SetGeneralBuluntu(models.Model):

    class Meta:
        verbose_name_plural = "Genel Buluntu Kayıt Formu"
        verbose_name = "Genel Buluntu Formu"


    INVENTORY_CHOICES = (
        ("1", "Etutluk"),
        ("2", "Envanterlik"),
        ("3", "Analiz"),
        ("4", "Diğer"),
    )

    BULUNTU_FORM_CHOICES = (

        ("1", "Pişmiş Toprak"),
        ("2", "Kemik"),
        ("3", "Taş"),
        ("4", "Metal"),
        ("5", "C14"),
        ("6", "Toprak Örneği"),
        ("7", "Çanak Çömlek")
    )

    storage = "Buluntu/Images"
    # methods
    year_choices = avaiable_years()
    letter_choices = generate_letters()
    number_choices = generate_numbers()

    year = models.IntegerField(
        ("Yıl Bilgisi"), choices=year_choices, default=current_year
    )
    date = models.DateField(("Buluntu Tarihi"), auto_now=False)
    plankareX = models.CharField(
        ("Plankare X"), max_length=4, choices=letter_choices, default="A"
    )
    plankareY = models.IntegerField(("Plankare Y"), choices=number_choices, default=1)

    plankareNo = models.CharField(("Plankare No"), max_length=50, null=True)

    gridX = models.CharField(("Grid X"), max_length=50)
    gridY = models.CharField(("Grid Y"), max_length=50)

    no = models.IntegerField(("Buluntu No"))
    noResult = models.CharField(("Buluntu No Sonuç"), max_length=50, null=True)
    secondaryNo = models.CharField(("Küçük Buluntu No"), default = "", max_length=150)

    type = models.ForeignKey(
        BuluntuTypes, to_field="buluntu", verbose_name=("Buluntu Türü"), on_delete=models.CASCADE
    )

    nivo = models.CharField(("Açılış Nivosu"), max_length=50)
    nivo_h = models.CharField(("Açılış Nivosu H"), max_length=50)
    shut_nivo = models.CharField(("Kapanış Nivosu"), max_length=50)
    shut_nivo_h = models.CharField(("Kapanış Nivosu H"), max_length=50)

    kor_x = models.CharField(("Kordinat X"), max_length=50)
    kor_y = models.CharField(("Kordinat Y"), max_length=50)
    kor_h = models.CharField(("Kordinat H"), max_length=50)

    area = models.ManyToManyField(
        BuluntuAlani, verbose_name=("Buluntu / Kova Alanı")
    )
    colour = models.ForeignKey(
        SetColour,
        to_field="color",
        verbose_name=("Buluntu Renk"),
        on_delete=models.CASCADE,
    )

    layer_count = models.CharField(("Tabaka Sayı"), max_length=50)
    layer_letter = models.CharField(("Tabaka Harf"), max_length=50)
    phase = models.CharField(("Evre"), max_length=50)
    period = models.ForeignKey(
        BuluntuPeriod, verbose_name=("Dönem"), on_delete=models.CASCADE)


    # genel tanımlamar
    definition = models.TextField(("Tanım"))
    description = models.TextField(("Genel Açıklama"))
    inventoryNo = models.CharField(("Envanter No"), max_length=50)
    pieceNo = models.CharField(("Eser No"), max_length=50)
    drawNo = models.CharField(("Çizim No"), max_length=50)
    inventories = models.CharField(("Etutluk / Envanter"), max_length=50, choices=INVENTORY_CHOICES)

    # görseller
    eskiz = models.ImageField(("Eskiz"), upload_to=storage, blank=True)
    picture = models.ImageField(("Fotoğraf"), upload_to=storage, blank=True)
    draw = models.ImageField(("Çizim"), upload_to=storage, blank=True)
    orto = models.ImageField(("OrtoFoto"), upload_to=storage, blank=True)

    # küçük buluntu
    buluntuForms = models.CharField(("Küçük Buluntu Formu"), max_length=50, choices=BULUNTU_FORM_CHOICES)
    filledBy = models.CharField(("Formu Dolduran"), max_length=50)
    processedBy = models.ForeignKey(SiteUser, verbose_name=("Veri Giren"), on_delete=models.CASCADE)



    def __str__(self) -> str:
        return f"{self.type} - {self.noResult}"



"""eser, durum, tür ve hayvan türü"""
class Piece(models.Model):
    name = models.CharField(("Eser Adı"), max_length=50)

    def __str__(self) -> str:
        return self.name

class Status(models.Model):
    status = models.CharField(("Durum"), max_length=50)

    def __str__(self) -> str:
        return self.status


class Tur(models.Model):
    type = models.CharField(("Tür"), max_length=50)

    def __str__(self) -> str:
        return self.type

class AnimalType(models.Model):

     type = models.CharField(("Hayvan Türü"), max_length=50)

     def __str__(self) -> str:
         return self.type


class YapimTeknik(models.Model):
    type = models.CharField(("Yapım Tekniği"), max_length=50)

    def __str__(self) -> str:
        return self.type

"""Renkler iç astar, dış astar hamur / çekirdek rengi """

class DisAstar(models.Model):

    data = models.CharField(("Dış Astar Rengi"), max_length=50)

    def __str__(self):
        return self.data

class IcAstar(models.Model):

    data = models.CharField(("İç Astar Rengi"), max_length=50)

    def __str__(self):
        return self.data


class HamurRenk(models.Model):

    data = models.CharField(("Hamur / Çekirdek Rengi"), max_length=50)

    def __str__(self):
        return self.data


""" Hamur Özellikleri """

class KatkiBoyut(models.Model):

    data = models.CharField(("Katkı Boyutu"), max_length=50)

    def __str__(self):
        return self.data


class Gozeneklilik(models.Model):

    data = models.CharField(("Gözeneklilik"), max_length=50)

    def __str__(self):
        return self.data


class Sertlik(models.Model):

    data = models.CharField(("Sertlik"), max_length=50)

    def __str__(self):
        return self.data

class Firinlama(models.Model):

    data = models.CharField(("Fırınlama"), max_length=50)

    def __str__(self):
        return self.data


class KatkiTur(models.Model):

    data = models.CharField(("Katkı Türü"), max_length=50)

    def __str__(self):
        return self.data

class YuzeyUygulamalari(models.Model):

    data = models.CharField(("Yüzey Uygulamaları"), max_length=50)

    def __str__(self):
        return self.data



"""Bezeme Alanı"""

class Bezeme(models.Model):
    data = models.CharField(("Bezeme"), max_length=50, default = "")

    def __str__(self):
        return self.data


class BezemeAlani(models.Model):

    data = models.CharField(("Bezeme Alanı"), max_length=50, default = "")

    def __str__(self):
        return self.data

class BezemeTuru(models.Model):

    data = models.CharField(("Bezeme Türü"), max_length=50, default = "")

    def __str__(self):
        return self.data


# analiz tüpü, plastik kutu vs.
class Miktar(models.Model):

    data = models.CharField(("Miktar"), max_length=50)

    def __str__(self):
        return self.data


"""Küçük Buluntu Modelleri"""


class Formlar(models.Model):

     class Meta:
        verbose_name = "Buluntu Form"
        verbose_name_plural = "Buluntu Formu"

     name = models.CharField(("Form Adı"), max_length=50)


     def __str__(self):
         return self.name


class RelatedField(models.Model):

    fieldName = models.CharField(("Alan Adı"), max_length=50)
    fieldType = models.CharField(("Veri"), max_length=50)
    # Diğer alanlar
    form = models.ForeignKey(Formlar, on_delete=models.CASCADE, related_name='related_fields')


class RelatedDropDown(models.Model):

    data = models.ForeignKey(Miktar, verbose_name=("Miktar"), on_delete=models.CASCADE, blank=True)
    form = models.ForeignKey(Formlar, on_delete=models.CASCADE, related_name='related_dropdown_fields')


class RelatedBezemesgKey(models.Model):

    bezeme = models.ForeignKey(Bezeme, on_delete=models.CASCADE, related_name='mtm', blank=True)
    bezemeAlani = models.ForeignKey(BezemeAlani, on_delete=models.CASCADE, related_name='mtm', blank=True)
    bezemeTuru = models.ForeignKey(BezemeTuru, on_delete=models.CASCADE, related_name='mtm', blank=True)
    form = models.ForeignKey(Formlar, on_delete=models.CASCADE)



class RelatedHamurKey(models.Model):

    katkiBoyut = models.ForeignKey(KatkiBoyut, on_delete=models.CASCADE, related_name='hamur_mtm', blank=True)
    gozeneklilik = models.ForeignKey(Gozeneklilik, on_delete=models.CASCADE, related_name='hamur_mtm', blank=True)
    sertlik = models.ForeignKey(Sertlik, on_delete=models.CASCADE, related_name='hamur_mtm', blank=True)
    firinlama = models.ForeignKey(Firinlama, on_delete=models.CASCADE, related_name='hamur_mtm', blank=True)
    katkiTur = models.ForeignKey(KatkiTur, on_delete=models.CASCADE, related_name='hamur_mtm', blank=True)
    yuzeyUygulamalari = models.ForeignKey(YuzeyUygulamalari, on_delete=models.CASCADE, related_name='hamur_mtm', blank=True)
    form = models.ForeignKey(Formlar, on_delete=models.CASCADE)



class Test(models.Model):

        AMOUNT_CHOICES = (

            ('1', "Analiz Tüpü"),
            ('2', "Plastik Kutu"),
            ('3', "Korunmuş Ahşap Örneği")
        )

        # türler
        piece = models.ForeignKey(Piece, verbose_name=("Eser Adı"), on_delete=models.CASCADE)
        status = models.ForeignKey(Status, verbose_name=("Durum"), on_delete=models.CASCADE)
        type = models.ForeignKey(Tur, verbose_name=("Tür"), on_delete=models.CASCADE)
        animalType = models.ForeignKey(AnimalType, verbose_name=("Hayvan Türü"), on_delete=models.CASCADE, default = "")
        yapimTeknik = models.ForeignKey(YapimTeknik, verbose_name=("Yapım Tekniği"), on_delete=models.CASCADE, default = "")
        # choices
        c14_choices = models.CharField(("Miktar"), choices=AMOUNT_CHOICES, max_length=50)

        # ölçüler
        amount = models.CharField(("Miktar"), max_length=50)
        flotasyonBefore = models.CharField(("Flotasyon Öncesi Miktar"), max_length=50)
        flotasyonAfter = models.CharField(("Flotasyon Sonrası Miktar"), max_length=50)
        defination = models.TextField(("Tanım"))

        width = models.CharField(("Yükseklik"), max_length=50)
        height = models.CharField(("Genişlik"), max_length=50)
        length = models.CharField(("Uzunluk"), max_length=50)
        size = models.CharField(("Kalınlık"), max_length=50)
        diameter = models.CharField(("Çap"), max_length=50)
        weight = models.CharField(("Ağırlık"), max_length=50)

        agizCap = models.CharField(("Ağız Çapı"), max_length=50,  default = "")
        kaideDip = models.CharField(("Kaide Dip Çapı"), max_length=50, default = "")
        govdeGenislik = models.CharField(("Gövde Genişliği"), max_length=50, default = "")
        kulpGenislik = models.CharField(("Kulp Genişliği Çapı"), max_length=50, default = "")
        cidarKalinlik = models.CharField(("Cidar Kalınlığı"), max_length=50, default = "")

        # renkler
        disAstar = models.ForeignKey(DisAstar, verbose_name=("Dış Astar Rengi"), on_delete=models.CASCADE)
        icAstar = models.ForeignKey(IcAstar, verbose_name=("İç Astar Rengi"), on_delete=models.CASCADE)
        hamurRenk = models.ForeignKey(HamurRenk, verbose_name=("Hamur / Çekirdek Rengi"), on_delete=models.CASCADE)

        # hamur
        firinlama = models.ForeignKey(Firinlama, verbose_name=("Fırınlama"), on_delete=models.CASCADE, default = "")
        katkiTur = models.ForeignKey(KatkiTur, verbose_name=("Katkı Türü"), on_delete=models.CASCADE, default = "")
        yuzeyUygulamari = models.ForeignKey(YuzeyUygulamalari, verbose_name=("Yüzey Uygulamaları"), on_delete=models.CASCADE, default = "")
        katki =  models.ForeignKey(KatkiBoyut, verbose_name=("Katkı Boyutu"), on_delete=models.CASCADE)
        gozeneklik = models.ForeignKey(Gozeneklilik, verbose_name=("Gözeneklilik"), on_delete=models.CASCADE)
        sertlik = models.ForeignKey(Sertlik, verbose_name=("Sertlik"), on_delete=models.CASCADE)

        # bezeme
        bezeme = models.ForeignKey(Bezeme, verbose_name=("Bezeme"), on_delete=models.CASCADE, default= "")
        bezemeAlani = models.ForeignKey(BezemeAlani, verbose_name=("Bezeme Alanı"), on_delete=models.CASCADE, default = "")
        bezemeTuru = models.ForeignKey(BezemeTuru, verbose_name=("Bezeme Türü"), on_delete=models.CASCADE, default = "")

        # class Meta:
        #     abstract = True
