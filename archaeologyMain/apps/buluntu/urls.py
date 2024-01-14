from django.urls import path

from .views import *


urlpatterns = [
    path("ekle", set_buluntu, name="set-buluntu"),
]
