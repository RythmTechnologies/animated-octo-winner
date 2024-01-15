from django.urls import path

from .views import *

urlpatterns = [
    path("ekle", get_rapor, name="set-rapor"),
    path("liste", get_rapor_list, name="rapor-liste"),
    path("delete/<id>", delete_rapor, name="delete-rapor"),
    path("update/<id>", update_rapor, name="update-rapor")
]
