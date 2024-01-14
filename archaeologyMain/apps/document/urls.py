from django.urls import path

from .views import get_document, get_document_list


urlpatterns = [
    path("ekle", get_document, name="set-document"),
    path("list", get_document_list, name="document-liste"),
]
