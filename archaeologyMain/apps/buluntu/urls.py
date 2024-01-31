from django.urls import path

from .views import *


urlpatterns = [
    path("ekle", set_buluntu, name="set-buluntu"),
    path("forms/<id>", get_buluntu_form, name="get-buluntu-form"),

]
