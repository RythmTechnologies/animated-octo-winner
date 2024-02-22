from django.urls import path

from .views import *


urlpatterns = [
    path("add", get_document, name="set-document"),
    path("list", get_document_list, name="document-liste"),
    path("delete/<id>", delete_document, name="delete-document"),
    path("update/<id>", update_document, name="update-document"),
    path('get-html/<id>/', get_html_content, name='get-html-content'),
]
