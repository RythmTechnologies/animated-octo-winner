from tinymce.models import HTMLField

from apps.logger.models import LoggableMixin

from django.db import models

from apps.specuser.models import *

from apps.main.mixin import TimeBasedStampModel


class BuluntuYeri(TimeBasedStampModel):
    name = models.CharField(("Buluntu Yeri"), max_length=150)

    def __str__(self) -> str:
        return self.name


class AcmaRapor(LoggableMixin, TimeBasedStampModel):
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
    rapordetail = HTMLField("Rapor Detay")
    file = models.FileField("Evrak Yükleme", upload_to="raporfiles",max_length=100)


    def save(self, *args, **kwargs):
        self.save_with_log(*args, **kwargs)


    def delete(self, *args, **kwargs):
        self.delete_with_log(*args, **kwargs)

    def __name__(self) ->str:
        return "Rapor"

    def __str__(self) -> str:
        return self.title
