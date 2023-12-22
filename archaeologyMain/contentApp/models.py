from django.db import models

from ckeditor.fields import RichTextField
from colorfield.fields import ColorField
from userApp.models import SiteUser

import datetime, string

class FixtureGainType(models.Model):
    input = models.CharField(("Alış Type"), max_length=50)

    def __str__(self) -> str:
        return self.input


# Demirbaş modelidir
class Fixture(models.Model):

    user = models.ForeignKey(
        SiteUser, verbose_name=("Kullanıcı"), on_delete=models.CASCADE
    )
    name = models.CharField(("Demirbaş Adı"), max_length=150)
    marka = models.CharField(("Marka"), max_length=150)
    model = models.CharField(("Model"), max_length=150)
    piece = models.IntegerField(("Adet"))
    unitprice = models.DecimalField(("Birim Fiyatı"), max_digits=15, decimal_places=2)
    taxrate = models.DecimalField(("Vergi Oranı"), max_digits=5, decimal_places=2)
    totalprice = models.DecimalField(("Toplam Fiyat"), max_digits=15, decimal_places=2)
    typeofaddition = models.OneToOneField(FixtureGainType, verbose_name=("Alış Şekli"), on_delete=models.CASCADE)
    dateofaddition = models.DateField(("Alım Tarihi"), auto_now_add=False)
    where = models.CharField(("Bulunduğu Yer"), max_length=150)
    custodian = models.CharField(("Zimmetli Kişi"), max_length=150)
    barcode = models.CharField(("Barkod Numarası"), max_length=150)
    companyName = models.CharField(("Firma Adı"), max_length=150)
    companyOfficial = models.CharField(("Firma Yetkilisi"), max_length=150)
    companyPhone = models.CharField(("Firma Telefon"), max_length=150)
    companyEmail = models.EmailField(("Firma E-Mail"), max_length=254)
    companyAddress = models.TextField(("Firma Adresi"))
    fixtureFile = models.FileField(
        ("Demirbaş Alım Belgesi"), upload_to="fixture", max_length=100
    )
    fixtureDescription = RichTextField(("Demirbaş Açıklama"), max_length=900)

    def __str__(self) -> str:
        return self.name

# Buluntu Yeri Açma Rapor İçin
class BuluntuYeri(models.Model):
    name = models.CharField(("Buluntu Yeri"), max_length=150)

    def __str__(self) -> str:
        return self.name


# Acma Rapor
class AcmaRapor(models.Model):
    user = models.ForeignKey(
        SiteUser, verbose_name=("Veri Giren"), on_delete=models.CASCADE
    )
    daily = models.BooleanField(("Günlük"), default=False)
    weekly = models.BooleanField(("Haftalık"), default=False)
    fifteenday = models.BooleanField(("15 Günlük"), default=False)
    monthly = models.BooleanField(("Aylık"), default=True)
    closing = models.BooleanField(("Kapanış"), default=True)
    placebuluntu = models.ManyToManyField(BuluntuYeri, verbose_name=("Buluntu Yeri"))
    rapordate = models.DateField(("Rapor Tarihi"), auto_now=False, auto_now_add=False)
    title = models.CharField(("Başlık"), max_length=150)
    owner = models.CharField(("Formu Dolduran"), max_length=150)
    rapordetail = RichTextField(("Rapor Detay"))
    file = models.FileField(("Evrak Yükleme"), upload_to="raporfiles", max_length=100)

    def __str__(self) -> str:
        return self.title


class DocumentCreateModel(models.Model):
    incomingdoc = models.BooleanField(("Gelen Evrak"), default=False)
    outgoingdoc = models.BooleanField(("Giden Evrak"), default=False)
    amount = models.BooleanField(("Tutanak"), default=False)
    high = models.BooleanField(("Yüksek"), default=False)
    middle = models.BooleanField(("Orta"), default=False)
    low = models.BooleanField(("Düşük"), default=False)
    docno = models.CharField(("Evrak No"), max_length=150)
    docdate = models.DateField(("Evrak Tarihi"), auto_now=False, auto_now_add=False)
    doccount = models.IntegerField(("Evrak Sayisi"))
    relevantunit = models.CharField(("İlgili Birim"), max_length=150)
    relevantinstitution = models.CharField(("İlgili Kurum"), max_length=150)
    docsubject = models.CharField(("Evrak Konusu"), max_length=150)
    user = models.OneToOneField(
        SiteUser, verbose_name=("Formu Dolduran"), on_delete=models.CASCADE
    )
    files = models.FileField(("Evrak Yükleme"), upload_to="document", max_length=100)
    detail = RichTextField(("Rapor Detay"))

    def __str__(self) -> str:
        return self.docsubject



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

    plankareNo = models.CharField(("Plankare No"), max_length=50, null = True)

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
        "contentApp.BuluntuAlani", verbose_name=("Buluntu / Kova Alanı")
    )
    colour = ColorField(default="#FF0000", verbose_name="Renk")

    layer_count = models.CharField(("Tabaka Sayı"), max_length=50)
    layer_letter = models.CharField(("Tabaka Harf"), max_length=50)
    phase = models.CharField(("Evre"), max_length=50)
    period = models.ForeignKey(
        "contentApp.BuluntuPeriod", verbose_name=("Dönem"), on_delete=models.CASCADE
    )

    # def __str__(self) -> str:
    #     return self.no

"""genel talimatlar modeli"""
class GeneralInstructions(models.Model):
    OPTION_CHOICES = (
    ("ETUTLUK", "Etutluk"),
    ("ENVANTERLIK", "Envanterlik"),
    ("ANALIZ", "Analiz"),
    ("DIGER", "Diğer"), )

    description = models.TextField(("Tanım"), max_length=250)
    description_2 = models.TextField(("Genel Açıklama"), max_length=250)
    inventoryNo = models.CharField(("Envanter No"), max_length=10)
    pieceNo = models.CharField(("Eser No"), max_length=10)
    illustrationNo = models.CharField(("Çizim No"), max_length=10)
    inventory = models.CharField(("Etütlük / Envanter"), max_length=30, choices=OPTION_CHOICES)

    def __str__(self) -> str:
        return self.description