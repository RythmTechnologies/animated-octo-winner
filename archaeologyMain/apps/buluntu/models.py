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
    buluntuForms = models.ForeignKey("buluntuForm.Formlar", verbose_name=("Küçük Buluntu"), default="1", on_delete=models.CASCADE)
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

# Diğer
class Cinsi(models.Model):
    data = models.CharField(("Cinsi"), max_length=50)


class Hammade(models.Model):
    data = models.CharField(("Ham Madde"), max_length=50)


class YongalamaUrunu(models.Model):
    data = models.CharField(("Yongalama Ürünü"), max_length=50)




