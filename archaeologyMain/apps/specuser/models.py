from django.db import models
from django.contrib.auth.models import AbstractUser


#Account Model Start
# types : admin, moderator, ogrenci
class SiteUser(AbstractUser):
    
    isModerator = models.BooleanField(("Moderatör mi"), default=False)
    isStudent = models.BooleanField(("Öğrenci mi"), default=False)


    def __str__(self) -> str:
        return self.username
#Account Model End