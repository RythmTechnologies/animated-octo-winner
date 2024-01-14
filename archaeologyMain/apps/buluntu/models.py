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
    buluntu = models.CharField(("Buluntu Türü"), max_length=30, unique=True)

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
    colorName = models.CharField(("Renk Adı"), max_length=20)
    color = ColorField(default="#FF0000", verbose_name="Renk Kodu", unique=True)

    def __str__(self) -> str:
        return self.colorName


"""buluntu ekle modeli"""


class SetGeneralBuluntu(models.Model):
    # methods
    year_choices = avaiable_years()
    letter_choices = generate_letters()
    number_choices = generate_numbers()

    user = models.ForeignKey(
        SiteUser, verbose_name=("Kullanıcı"), on_delete=models.CASCADE
    )
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
    secondaryNo = models.IntegerField(("Küçük Buluntu No"))

    type = models.ForeignKey(
        BuluntuTypes, to_field="buluntu", verbose_name=("Tür"), on_delete=models.CASCADE
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
        BuluntuPeriod, verbose_name=("Dönem"), on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return str(self.no)


"""genel tanımlamalar modeli"""


class GeneralInstructions(models.Model):
    OPTION_CHOICES = (
        ("ETUTLUK", "Etutluk"),
        ("ENVANTERLIK", "Envanterlik"),
        ("ANALIZ", "Analiz"),
        ("DIGER", "Diğer"),
    )

    buluntu = models.ForeignKey(
        SetGeneralBuluntu,
        null=True,
        verbose_name=("Buluntu"),
        on_delete=models.CASCADE,
    )
    description = models.TextField(("Tanım"), max_length=250)
    description_2 = models.TextField(("Genel Açıklama"), max_length=250)
    inventoryNo = models.CharField(("Envanter No"), max_length=10)
    pieceNo = models.CharField(("Eser No"), max_length=10)
    illustrationNo = models.CharField(("Çizim No"), max_length=10)
    inventory = models.CharField(
        ("Etütlük / Envanter"), max_length=30, choices=OPTION_CHOICES
    )

    def __str__(self) -> str:
        return self.description


"""İlişkili: SetGeneralBuluntu Fotoğraflar bu model atlında depolanır"""


class BuluntuImages(models.Model):
    store = "Buluntu/Attachments"

    buluntu = models.ForeignKey(
        SetGeneralBuluntu,
        null=True,
        verbose_name=("Buluntu"),
        on_delete=models.CASCADE,
    )
    type_1 = models.ImageField(("Eskiz"), upload_to=store)
    type_2 = models.ImageField(("Fotoğraf"), upload_to=store)
    type_3 = models.ImageField(("Çizim"), upload_to=store)
    type_4 = models.ImageField(("OrtoFoto"), upload_to=store)


"""Küçük Buluntu Formu Yardımcı Modelleri"""


class Pieces(models.Model):
    name = models.CharField(("Eser Adı"), max_length=100)
    status = models.CharField(("Eser Durumu"), max_length=50, default="")

    def __str__(self) -> str:
        return self.name


"""Küçük Buluntu Formu Yardımcı Modelleri Biter"""

"""Renkler (Astar) formu"""


class AstarColour(models.Model):
    disAstar = models.CharField(("Dış Astar Rengi"), max_length=50)
    icAstar = models.CharField(("İç Astar Rengi"), max_length=50)
    hamur = models.CharField(("Hamur / Çekirdek Rengi"), max_length=50)

    def __str__(self) -> str:
        return self.disAstar


"""Hamur Özellikleri Formu"""


class HamurKatkiBoy(models.Model):
    value = models.CharField(("Katkı Boyutu"), max_length=50)

    def __str__(self) -> str:
        return self.value


class HamurGozeneklilik(models.Model):
    value = models.CharField(("Gözeneklilik"), max_length=50)

    def __str__(self) -> str:
        return self.value


class HamurSertlik(models.Model):
    value = models.CharField(("Sertlik"), max_length=50)

    def __str__(self) -> str:
        return self.value


class HamurFirinlama(models.Model):
    value = models.CharField(("Fırınlama"), max_length=50)

    def __str__(self) -> str:
        return self.value


class HamurKatkiTur(models.Model):
    value = models.CharField(("Katkı Türü"), max_length=50)

    def __str__(self) -> str:
        return self.value


class HamurYuzey(models.Model):
    value = models.CharField(("Yuzey Ugulamaları"), max_length=50)

    def __str__(self) -> str:
        return self.value


"""Hamur Özellikleri Formu Biter"""


"""Benzeme Formu"""


class Bezeme(models.Model):
    bezeme = models.CharField(("Bezeme"), max_length=50)
    bezemeAlani = models.CharField(("Bezeme Alanı"), max_length=50)
    bezemeTur = models.CharField(("Bezeme Türü"), max_length=50)

    def __str__(self) -> str:
        return self.bezeme


"""küçük buluntu formu"""


class MinorBuluntuForm(models.Model):
    # şimdilik charfield
    buluntuName = models.CharField(("Buluntu Adı"), max_length=50, default="")
    piece = models.ForeignKey(
        Pieces,
        verbose_name=("Eser"),
        on_delete=models.CASCADE,
        related_name="eserler",
        default="",
    )
    width = models.CharField(("Yükseklik"), max_length=50, default="", blank=True)
    thick = models.CharField(("Kalınlık"), max_length=50, default="", blank=True)
    height = models.CharField(("Genişlik"), max_length=50, default="", blank=True)
    diameter = models.CharField(("Çap"), max_length=50, default="", blank=True)
    length = models.CharField(("Uzunluk"), max_length=50, default="", blank=True)
    weight = models.CharField(("Ağırlık"), max_length=50, default="", blank=True)
    color = models.ForeignKey(
        AstarColour, verbose_name=("Renkler"), on_delete=models.CASCADE, default=""
    )
    hamurBoy = models.ForeignKey(
        HamurKatkiBoy,
        verbose_name=("Katkı Boyutu"),
        on_delete=models.CASCADE,
        default="",
    )
    hamurGozeneklik = models.ForeignKey(
        HamurGozeneklilik,
        verbose_name=("Gözeneklilik"),
        on_delete=models.CASCADE,
        default="",
    )
    hamurSertlik = models.ForeignKey(
        HamurSertlik, verbose_name=("Sertlik"), on_delete=models.CASCADE, default=""
    )
    hamurFirinlama = models.ForeignKey(
        HamurFirinlama, verbose_name=("Fırınlama"), on_delete=models.CASCADE, default=""
    )
    hamurTur = models.ForeignKey(
        HamurKatkiTur, verbose_name=("Katkı Türü"), on_delete=models.CASCADE, default=""
    )
    hamurYuzey = models.ForeignKey(
        HamurYuzey,
        verbose_name=("Hamur Yüzey Uygulamaları"),
        on_delete=models.CASCADE,
        default="",
    )
    bezeme = models.ForeignKey(
        Bezeme, verbose_name=("Bezeme"), on_delete=models.CASCADE, default=""
    )

    # tanım ve ölçüler ?

    def __str__(self) -> str:
        return self.buluntuName


"""küçük buluntu modeli"""


class MinorBuluntu(models.Model):
    OPTION_CHOICES = (
        ("1", "El Arabası"),
        ("2", "Insitu/Dolgu"),
        ("3", "Tum"),
        ("4", "Kirik"),
    )

    buluntu = models.CharField(("Küçük Buluntu"), max_length=50, choices=OPTION_CHOICES)
    filledBy = models.CharField(("Formu Dolduran"), max_length=50)
    processedBy = models.CharField(("Veri Giren"), max_length=50)
    form = models.ForeignKey(
        MinorBuluntuForm,
        verbose_name=("Küçük Buluntu Formu"),
        default="",
        on_delete=models.CASCADE,
    )
