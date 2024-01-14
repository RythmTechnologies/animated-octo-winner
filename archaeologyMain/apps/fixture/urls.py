from django.urls import path

from .views import *


urlpatterns = [
    path("ekle", set_fixture, name="set-fixture"),
    path("liste", fixture_list, name="fixture-liste"),
]
