from django.db import models

from apps.specuser.models import *

from gdstorage.storage import GoogleDriveStorage, GoogleDrivePermissionType, GoogleDrivePermissionRole, GoogleDriveFilePermission

permission =  GoogleDriveFilePermission(
   GoogleDrivePermissionRole.READER,
   GoogleDrivePermissionType.USER,
   "codermungan@gmail.com"
)

public_permission = GoogleDriveFilePermission(
    GoogleDrivePermissionRole.READER,
    GoogleDrivePermissionType.ANYONE,
    None
)

drive_storage = GoogleDriveStorage(permissions=(permission, public_permission, ))


class BuluntuYeri(models.Model):
    name = models.CharField(("Buluntu Yeri"), max_length=150)

    def __str__(self) -> str:
        return self.name


class AcmaRapor(models.Model):
    RAPOR_CHOICES = (
        ("daily", "Günlük"),
        ("weekly", "Haftalık"),
        ("fifteenday", "15 Günlük"),
        ("monthly", "Aylık"),
        ("closing", "Kapanış"),
    )
    user = models.ForeignKey(
        SiteUser, verbose_name="Veri Giren", on_delete=models.CASCADE
    )
    rapor_type = models.CharField(
        "Rapor Tipi", max_length=10, choices=RAPOR_CHOICES, default="daily"
    )
    placebuluntu = models.ForeignKey(
        BuluntuYeri, verbose_name="Buluntu Yeri", on_delete=models.CASCADE
    )
    rapordate = models.DateField("Rapor Tarihi", auto_now=False, auto_now_add=False)
    title = models.CharField("Başlık", max_length=150)
    owner = models.CharField("Formu Dolduran", max_length=150)
    rapordetail = models.TextField("Rapor Detay")
    file = models.FileField("Evrak Yükleme", upload_to="raporfiles",storage=drive_storage,max_length=100)

    def __str__(self) -> str:
        return self.title
