from django.db import models
from django.utils import timezone
from apps.specuser.models import SiteUser

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from apps.main.mixin import TimeBasedStampModel


# Create your models here.
class LogEntry(TimeBasedStampModel):
    user = models.ForeignKey(SiteUser, verbose_name=("Kullanıcı"), on_delete=models.SET_NULL, null=True, related_name='log_entries')
    action = models.CharField(("İşlem"), max_length=50)

    description = models.TextField(("Açıklama"))
    timestamp = models.DateTimeField(("Zaman Damgası"),default=timezone.now)

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_related",  # Benzersiz bir related_name
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    def __str__(self) -> str:
        return f"{self.user} {self.action} at {self.timestamp}"

class LoggableMixin:
    def save_with_log(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        is_create = self._state.adding

        super().save(*args, **kwargs)

        action = "oluşturuldu" if is_create else "güncellendi"
        LogEntry.objects.create(
            user=user,
            action=action,
            description=f"{self.__class__.__str__(self)}, {self.__name__()} {action}",
            timestamp=timezone.now(),
            content_type=ContentType.objects.get_for_model(self.__class__),
            object_id=self.id
        )

    def delete_with_log(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        content_type = ContentType.objects.get_for_model(self.__class__)
        object_id = self.id

        super().delete(*args, **kwargs)

        if user:
            LogEntry.objects.create(
                user=user,
                action="silindi",
                description=f"{self.__class__.__str__(self)} , {self.__name__()} silindi .",
                timestamp=timezone.now(),
                content_type=content_type,
                object_id=object_id
            )