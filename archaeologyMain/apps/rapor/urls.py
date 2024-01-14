from django.urls import path

from .views import *

urlpatterns = [
    path("ekle", get_rapor, name="set-rapor"),
    path("liste", get_rapor_list, name="rapor-liste"),
]
