from django.urls import path

from .views import *


urlpatterns = [
    path("dashboard", get_dashboard, name="dashboard"),
    path("buluntu/ekle", set_buluntu, name="set-buluntu"),
    path("fixture/ekle", set_fixture, name="set-fixture"),
    path("fixture/liste", fixture_list, name="fixture-liste"),
    path("rapor/ekle", get_rapor, name="set-rapor"),
    path("rapor/liste", get_rapor_list, name="rapor-liste"),
    path("document/ekle", get_document, name="set-document"),
    path("document/list", get_document_list, name="document-liste"),
]
