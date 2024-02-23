from django.urls import path

from .views import *


urlpatterns = [
    path("ekle", set_buluntu, name="set-buluntu"),
    path("ekle/test", get_buluntu_test, name="get-buluntu-test"),
    path("forms/<formId>", get_buluntu_form, name="get-or-set-buluntu-form"),
]
