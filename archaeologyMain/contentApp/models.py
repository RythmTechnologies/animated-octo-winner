from django.db import models

from ckeditor.fields import RichTextField

from userApp.models import SiteUser


class Fixture(models.Model):
    name = models.CharField(("Demirbaş Adı"), max_length=150)
    marka = models.CharField(("Marka"), max_length=150)
    model = models.CharField(("Model"), max_length=150)
    piece = models.IntegerField(("Adet"))
    unitprice = models.DecimalField(("Birim Fiyatı"), max_digits=15, decimal_places=2)
    taxrate = models.DecimalField(("Vergi Oranı"), max_digits=5, decimal_places=2)
    totalprice = models.DecimalField(("Toplam Fiyat"), max_digits=15, decimal_places=2)
    typeofaddition = models.CharField(("Alış Şekli"), max_length=150)
    dateofaddition = models.DateField(("Alım Tarihi"), auto_now_add=True)
    where = models.CharField(("Bulunduğu Yer"), max_length=150)
    custodian = models.CharField(("Zimmetli Kişi"), max_length=150)
    barcode = models.CharField(("Barkod Numarası"), max_length=150)

    def __str__(self) -> str:
        return self.name
    
class CompanyInfo(models.Model):
    fixture = models.ForeignKey(Fixture, verbose_name=("Demirbaş"), on_delete=models.CASCADE)
    companyName = models.CharField(("Firma Adı"), max_length=150)
    companyOfficial = models.CharField(("Firma Yetkilisi"), max_length=150)
    companyPhone = models.CharField(("Firma Adı"), max_length=150)
    companyEmail = models.EmailField(("Firma E-Mail"), max_length=254)
    companyAddress = models.TextField(("Firma Adresi"))

    def __str__(self) -> str:
        return self.companyName
    

class FixtureInfo(models.Model):
    fixture = models.ForeignKey(Fixture, verbose_name=("Demirbaş"), on_delete=models.CASCADE)
    fixtureFile = models.FileField(("Demirbaş Alım Belgesi"), upload_to="fixture", max_length=100)
    fixtureDescription = RichTextField(("Demirbaş Açıklama"),max_length=900)

    def __str__(self) -> str:
        return self.fixture